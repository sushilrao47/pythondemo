import React, { useState, useRef } from "react";
import ReactFlow, {
  ReactFlowProvider,
  Controls,
  Background,
  addEdge,
  removeElements
} from "react-flow-renderer";

import Sidebar from "./Sidebar";
import clinetData from "./clientData.json";

// import "./dnd.css";

const initialElements = [
  {
    id: "1",
    type: "input",
    data: { label: "input node" },
    sourcePosition: "right",
    targetPosition: "left",
    position: { x: 250, y: 5 }
  }
];

const generateNodesFromValueChain = (valuChain) => {
  const elements = [];
  const valueChainSize = Object.keys(valuChain).length;
  const firstNodeXPosition = window.innerWidth / valueChainSize;
  const firstNodeYPosition = window.innerHeight / valueChainSize;
  let positionIncreamentCount = 1;
  for (const valuChainItem in valuChain) {
    if (Object.hasOwnProperty.call(valuChain, valuChainItem)) {
      const element = valuChain[valuChainItem];
      const position = {
        x: firstNodeXPosition * positionIncreamentCount,
        y: firstNodeYPosition * positionIncreamentCount
      };
      positionIncreamentCount++;
      elements.push({
        id: valuChainItem,
        type: element.childOf ? "default" : "output",
        data: { label: element.label },
        position,
        sourcePosition: "right",
        targetPosition: "left"
      });
    }
  }
  return elements;
};

const generateEdgesFromValueChain = (valuChain) => {
  const elements = [];
  for (const valuChainItem in valuChain) {
    if (Object.hasOwnProperty.call(valuChain, valuChainItem)) {
      const element = valuChain[valuChainItem];
      if (element.childOf) {
        elements.push({
          id: `edge-${valuChainItem}-${element.childOf}`,
          source: valuChainItem,
          target: element.childOf,
          type: "smoothstep"
        });
      }
    }
  }
  return elements;
};

let id = 0;
const getId = () => `dndnode_${id++}`;

const DnDFlow = () => {
  const [paneMoveable] = useState(false);
  const [panOnScroll] = useState(true);
  const reactFlowWrapper = useRef(null);
  const [reactFlowInstance, setReactFlowInstance] = useState(null);
  const [elements, setElements] = useState(initialElements);

  const onLoad = (_reactFlowInstance) => {
    setReactFlowInstance(_reactFlowInstance);

    // Set Nodes
    setElements((es) =>
      es.concat(generateNodesFromValueChain(clinetData.valueChain))
    );
    // Set Edges
    setElements((es) =>
      es.concat(generateEdgesFromValueChain(clinetData.valueChain))
    );
  };

  const onConnect = (params) => setElements((els) => addEdge(params, els));
  const onElementsRemove = (elementsToRemove) =>
    setElements((els) => removeElements(elementsToRemove, els));

  const onNodeDoubleClick = (event, node) => {
    // node.data.label = "This is it";
    console.log(node);
  };

  const onDragOver = (event) => {
    event.preventDefault();
    event.dataTransfer.dropEffect = "move";
  };

  const onDrop = (event) => {
    event.preventDefault();

    const reactFlowBounds = reactFlowWrapper.current.getBoundingClientRect();
    const type = event.dataTransfer.getData("application/reactflow");
    const position = reactFlowInstance.project({
      x: event.clientX - reactFlowBounds.left,
      y: event.clientY - reactFlowBounds.top
    });
    const newNode = {
      id: getId(),
      type,
      position,
      sourcePosition: "right",
      targetPosition: "left",
      data: { label: `${type} node` }
    };

    setElements((es) => es.concat(newNode));
  };

  return (
    <div className="dndflow">
      <ReactFlowProvider>
        <div className="reactflow-wrapper" ref={reactFlowWrapper}>
          <ReactFlow
            elements={elements}
            onConnect={onConnect}
            onElementsRemove={onElementsRemove}
            onLoad={onLoad}
            onDrop={onDrop}
            onDragOver={onDragOver}
            paneMoveable={paneMoveable}
            panOnScroll={panOnScroll}
            snapToGrid={true}
            onNodeDoubleClick={onNodeDoubleClick}
          >
            <Controls />
            <Background variant="lines" />
          </ReactFlow>
        </div>
        <Sidebar />
      </ReactFlowProvider>
    </div>
  );
};

export default DnDFlow;
