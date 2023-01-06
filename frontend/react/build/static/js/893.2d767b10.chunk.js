"use strict";(self.webpackChunkcedri_ugv_dashboard=self.webpackChunkcedri_ugv_dashboard||[]).push([[893],{28308:function(e,i,t){t.d(i,{Z:function(){return P}});var n=t(29439),r=t(47313),a=t(30168),o=t(63366),s=t(87462),l=t(83061),d=t(30686),c=t(21921);function h(e){return String(e).match(/[\d.\-+]*\s*(.*)/)[1]||""}function u(e){return parseFloat(e)}var m=t(17551),x=t(64164),g=t(11236),Z=t(77430),p=t(32298);function j(e){return(0,p.Z)("MuiSkeleton",e)}(0,Z.Z)("MuiSkeleton",["root","text","rectangular","rounded","circular","pulse","wave","withChildren","fitContent","heightAuto"]);var v,b,f,y,S,H,w,L,B=t(46417),k=["animation","className","component","height","style","variant","width"],C=(0,d.F4)(S||(S=v||(v=(0,a.Z)(["\n  0% {\n    opacity: 1;\n  }\n\n  50% {\n    opacity: 0.4;\n  }\n\n  100% {\n    opacity: 1;\n  }\n"])))),R=(0,d.F4)(H||(H=b||(b=(0,a.Z)(["\n  0% {\n    transform: translateX(-100%);\n  }\n\n  50% {\n    /* +0.5s of delay between each loop */\n    transform: translateX(100%);\n  }\n\n  100% {\n    transform: translateX(100%);\n  }\n"])))),F=(0,x.ZP)("span",{name:"MuiSkeleton",slot:"Root",overridesResolver:function(e,i){var t=e.ownerState;return[i.root,i[t.variant],!1!==t.animation&&i[t.animation],t.hasChildren&&i.withChildren,t.hasChildren&&!t.width&&i.fitContent,t.hasChildren&&!t.height&&i.heightAuto]}})((function(e){var i=e.theme,t=e.ownerState,n=h(i.shape.borderRadius)||"px",r=u(i.shape.borderRadius);return(0,s.Z)({display:"block",backgroundColor:i.vars?i.vars.palette.Skeleton.bg:(0,m.Fq)(i.palette.text.primary,"light"===i.palette.mode?.11:.13),height:"1.2em"},"text"===t.variant&&{marginTop:0,marginBottom:0,height:"auto",transformOrigin:"0 55%",transform:"scale(1, 0.60)",borderRadius:"".concat(r).concat(n,"/").concat(Math.round(r/.6*10)/10).concat(n),"&:empty:before":{content:'"\\00a0"'}},"circular"===t.variant&&{borderRadius:"50%"},"rounded"===t.variant&&{borderRadius:(i.vars||i).shape.borderRadius},t.hasChildren&&{"& > *":{visibility:"hidden"}},t.hasChildren&&!t.width&&{maxWidth:"fit-content"},t.hasChildren&&!t.height&&{height:"auto"})}),(function(e){return"pulse"===e.ownerState.animation&&(0,d.iv)(w||(w=f||(f=(0,a.Z)(["\n      animation: "," 1.5s ease-in-out 0.5s infinite;\n    "]))),C)}),(function(e){var i=e.ownerState,t=e.theme;return"wave"===i.animation&&(0,d.iv)(L||(L=y||(y=(0,a.Z)(["\n      position: relative;\n      overflow: hidden;\n\n      /* Fix bug in Safari https://bugs.webkit.org/show_bug.cgi?id=68196 */\n      -webkit-mask-image: -webkit-radial-gradient(white, black);\n\n      &::after {\n        animation: "," 1.6s linear 0.5s infinite;\n        background: linear-gradient(\n          90deg,\n          transparent,\n          ",",\n          transparent\n        );\n        content: '';\n        position: absolute;\n        transform: translateX(-100%); /* Avoid flash during server-side hydration */\n        bottom: 0;\n        left: 0;\n        right: 0;\n        top: 0;\n      }\n    "]))),R,(t.vars||t).palette.action.hover)})),q=r.forwardRef((function(e,i){var t=(0,g.Z)({props:e,name:"MuiSkeleton"}),n=t.animation,r=void 0===n?"pulse":n,a=t.className,d=t.component,h=void 0===d?"span":d,u=t.height,m=t.style,x=t.variant,Z=void 0===x?"text":x,p=t.width,v=(0,o.Z)(t,k),b=(0,s.Z)({},t,{animation:r,component:h,variant:Z,hasChildren:Boolean(v.children)}),f=function(e){var i=e.classes,t=e.variant,n=e.animation,r=e.hasChildren,a=e.width,o=e.height,s={root:["root",t,n,r&&"withChildren",r&&!a&&"fitContent",r&&!o&&"heightAuto"]};return(0,c.Z)(s,j,i)}(b);return(0,B.jsx)(F,(0,s.Z)({as:h,ref:i,className:(0,l.Z)(f.root,a),ownerState:b},v,{style:(0,s.Z)({width:p,height:u},m)}))})),W=t(62463),z=t(82937),M=t(76657),P=function(e){var i=e.children,t=(0,r.useState)(!0),a=(0,n.Z)(t,2),o=a[0],s=a[1];(0,r.useEffect)((function(){s(!1)}),[]);var l=(0,B.jsx)(M.Z,{title:(0,B.jsx)(q,{sx:{width:{xs:120,md:180}}}),secondary:(0,B.jsx)(q,{animation:"wave",variant:"circular",width:24,height:24}),children:(0,B.jsxs)(W.Z,{spacing:1,children:[(0,B.jsx)(q,{}),(0,B.jsx)(q,{sx:{height:64},animation:"wave",variant:"rectangular"}),(0,B.jsx)(q,{}),(0,B.jsx)(q,{})]})});return(0,B.jsxs)(B.Fragment,{children:[o&&(0,B.jsxs)(z.ZP,{container:!0,spacing:3,children:[(0,B.jsx)(z.ZP,{item:!0,xs:12,md:6,children:l}),(0,B.jsx)(z.ZP,{item:!0,xs:12,md:6,children:l}),(0,B.jsx)(z.ZP,{item:!0,xs:12,md:6,children:l}),(0,B.jsx)(z.ZP,{item:!0,xs:12,md:6,children:l})]}),!o&&i]})}},47893:function(e,i,t){t.r(i);var n=t(82937),r=t(62463),a=t(42669),o=t(80493),s=t(63509),l=t(77449),d=t(28308),c=t(76657),h=t(46417);i.default=function(){return(0,h.jsx)(d.Z,{children:(0,h.jsxs)(n.ZP,{container:!0,spacing:3,children:[(0,h.jsx)(n.ZP,{item:!0,xs:12,lg:6,children:(0,h.jsxs)(r.Z,{spacing:3,children:[(0,h.jsx)(c.Z,{title:"Basic",codeHighlight:!0,children:(0,h.jsxs)(r.Z,{spacing:.75,sx:{mt:-1.5},children:[(0,h.jsx)(a.Z,{variant:"h1",children:"Inter"}),(0,h.jsx)(a.Z,{variant:"h5",children:"Font Family"}),(0,h.jsxs)(o.Z,{"aria-label":"breadcrumb",children:[(0,h.jsx)(a.Z,{variant:"h6",children:"Regular"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Medium"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Bold"})]})]})}),(0,h.jsx)(c.Z,{title:"Heading",codeHighlight:!0,children:(0,h.jsxs)(r.Z,{spacing:2,children:[(0,h.jsx)(a.Z,{variant:"h1",children:"H1 Heading"}),(0,h.jsxs)(o.Z,{"aria-label":"breadcrumb",children:[(0,h.jsx)(a.Z,{variant:"h6",children:"Size: 38px"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Weight: Bold"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Line Height: 46px"})]}),(0,h.jsx)(s.Z,{}),(0,h.jsx)(a.Z,{variant:"h2",children:"H2 Heading"}),(0,h.jsxs)(o.Z,{"aria-label":"breadcrumb",children:[(0,h.jsx)(a.Z,{variant:"h6",children:"Size: 30px"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Weight: Bold"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Line Height: 38px"})]}),(0,h.jsx)(s.Z,{}),(0,h.jsx)(a.Z,{variant:"h3",children:"H3 Heading"}),(0,h.jsxs)(o.Z,{"aria-label":"breadcrumb",children:[(0,h.jsx)(a.Z,{variant:"h6",children:"Size: 24px"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Weight: Regular & Bold"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Line Height: 32px"})]}),(0,h.jsx)(s.Z,{}),(0,h.jsx)(a.Z,{variant:"h4",children:"H4 Heading"}),(0,h.jsxs)(o.Z,{"aria-label":"breadcrumb",children:[(0,h.jsx)(a.Z,{variant:"h6",children:"Size: 20px"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Weight: Bold"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Line Height: 28px"})]}),(0,h.jsx)(s.Z,{}),(0,h.jsx)(a.Z,{variant:"h5",children:"H5 Heading"}),(0,h.jsxs)(o.Z,{"aria-label":"breadcrumb",children:[(0,h.jsx)(a.Z,{variant:"h6",children:"Size: 16px"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Weight: Regular & Medium & Bold"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Line Height: 24px"})]}),(0,h.jsx)(s.Z,{}),(0,h.jsx)(a.Z,{variant:"h6",children:"H6 Heading / Subheading"}),(0,h.jsxs)(o.Z,{"aria-label":"breadcrumb",children:[(0,h.jsx)(a.Z,{variant:"h6",children:"Size: 14px"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Weight: Regular"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Line Height: 22px"})]})]})}),(0,h.jsx)(c.Z,{title:"Body 1",codeHighlight:!0,children:(0,h.jsxs)(h.Fragment,{children:[(0,h.jsx)(a.Z,{variant:"body1",gutterBottom:!0,children:"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."}),(0,h.jsxs)(o.Z,{"aria-label":"breadcrumb",children:[(0,h.jsx)(a.Z,{variant:"h6",children:"Size: 14px"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Weight: Regular"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Line Height: 22px"})]})]})}),(0,h.jsx)(c.Z,{title:"Body 2",codeHighlight:!0,children:(0,h.jsxs)(h.Fragment,{children:[(0,h.jsx)(a.Z,{variant:"body2",gutterBottom:!0,children:"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."}),(0,h.jsxs)(o.Z,{"aria-label":"breadcrumb",children:[(0,h.jsx)(a.Z,{variant:"h6",children:"Size: 12px"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Weight: Regular"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Line Height: 20px"})]})]})}),(0,h.jsx)(c.Z,{title:"Subtitle 1",codeHighlight:!0,children:(0,h.jsxs)(h.Fragment,{children:[(0,h.jsx)(a.Z,{variant:"subtitle1",gutterBottom:!0,children:"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."}),(0,h.jsxs)(o.Z,{"aria-label":"breadcrumb",children:[(0,h.jsx)(a.Z,{variant:"h6",children:"Size: 14px"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Weight: Medium"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Line Height: 22px"})]})]})}),(0,h.jsx)(c.Z,{title:"Subtitle 2",codeHighlight:!0,children:(0,h.jsxs)(h.Fragment,{children:[(0,h.jsx)(a.Z,{variant:"subtitle2",gutterBottom:!0,children:"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."}),(0,h.jsxs)(o.Z,{"aria-label":"breadcrumb",children:[(0,h.jsx)(a.Z,{variant:"h6",children:"Size: 12px"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Weight: Medium"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Line Height: 20px"})]})]})}),(0,h.jsx)(c.Z,{title:"Caption",codeHighlight:!0,children:(0,h.jsxs)(r.Z,{spacing:1,children:[(0,h.jsx)(a.Z,{variant:"caption",children:"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."}),(0,h.jsxs)(o.Z,{"aria-label":"breadcrumb",children:[(0,h.jsx)(a.Z,{variant:"h6",children:"Size: 12px"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Weight: Regular"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Line Height: 20px"})]})]})})]})}),(0,h.jsx)(n.ZP,{item:!0,xs:12,lg:6,children:(0,h.jsxs)(r.Z,{spacing:3,children:[(0,h.jsx)(c.Z,{title:"Alignment",codeHighlight:!0,children:(0,h.jsxs)(h.Fragment,{children:[(0,h.jsx)(a.Z,{variant:"body2",gutterBottom:!0,children:"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."}),(0,h.jsx)(a.Z,{variant:"body2",textAlign:"center",gutterBottom:!0,children:"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."}),(0,h.jsx)(a.Z,{variant:"body2",textAlign:"right",children:"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."})]})}),(0,h.jsx)(c.Z,{title:"Gutter Bottom",codeHighlight:!0,children:(0,h.jsxs)(h.Fragment,{children:[(0,h.jsx)(a.Z,{variant:"body1",gutterBottom:!0,children:"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."}),(0,h.jsx)(a.Z,{variant:"body2",gutterBottom:!0,children:"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."}),(0,h.jsxs)(o.Z,{"aria-label":"breadcrumb",children:[(0,h.jsx)(a.Z,{variant:"h6",children:"Size: 12px"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Weight: Regular"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Line Height: 20px"})]})]})}),(0,h.jsx)(c.Z,{title:"Overline",codeHighlight:!0,children:(0,h.jsxs)(r.Z,{spacing:1.5,children:[(0,h.jsx)(a.Z,{variant:"overline",children:"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."}),(0,h.jsxs)(o.Z,{"aria-label":"breadcrumb",children:[(0,h.jsx)(a.Z,{variant:"h6",children:"Size: 12px"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Weight: Regular"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Line Height: 20px"})]})]})}),(0,h.jsx)(c.Z,{title:"Link",codeHighlight:!0,children:(0,h.jsxs)(r.Z,{spacing:1.5,children:[(0,h.jsx)(l.Z,{href:"#",children:"www.mantis.com"}),(0,h.jsxs)(o.Z,{"aria-label":"breadcrumb",children:[(0,h.jsx)(a.Z,{variant:"h6",children:"Size: 12px"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Weight: Regular"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Line Height: 20px"})]})]})}),(0,h.jsx)(c.Z,{title:"Colors",codeHighlight:!0,children:(0,h.jsxs)(h.Fragment,{children:[(0,h.jsx)(a.Z,{variant:"h6",color:"textPrimary",gutterBottom:!0,children:"This is textPrimary text color."}),(0,h.jsx)(a.Z,{variant:"h6",color:"textSecondary",gutterBottom:!0,children:"This is textSecondary text color."}),(0,h.jsx)(a.Z,{variant:"h6",color:"primary",gutterBottom:!0,children:"This is primary text color."}),(0,h.jsx)(a.Z,{variant:"h6",color:"secondary",gutterBottom:!0,children:"This is secondary text color."}),(0,h.jsx)(a.Z,{variant:"h6",color:"success",gutterBottom:!0,children:"This is success text color."}),(0,h.jsx)(a.Z,{variant:"h6",sx:{color:"warning.main"},gutterBottom:!0,children:"This is warning text color."}),(0,h.jsx)(a.Z,{variant:"h6",color:"error",gutterBottom:!0,children:"This is error text color."})]})}),(0,h.jsx)(c.Z,{title:"Paragraph",codeHighlight:!0,children:(0,h.jsxs)(h.Fragment,{children:[(0,h.jsx)(a.Z,{variant:"body1",gutterBottom:!0,children:"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."}),(0,h.jsxs)(o.Z,{"aria-label":"breadcrumb",children:[(0,h.jsx)(a.Z,{variant:"h6",children:"Size: 14px"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Weight: Regular"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Line Height: 22px"})]})]})}),(0,h.jsx)(c.Z,{title:"Font Style",codeHighlight:!0,children:(0,h.jsxs)(h.Fragment,{children:[(0,h.jsx)(a.Z,{variant:"body1",gutterBottom:!0,sx:{fontStyle:"italic"},children:"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."}),(0,h.jsx)(a.Z,{variant:"subtitle1",gutterBottom:!0,sx:{fontStyle:"italic"},children:"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."}),(0,h.jsxs)(o.Z,{"aria-label":"breadcrumb",children:[(0,h.jsx)(a.Z,{variant:"h6",children:"Size: 14px"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Weight: Italic Regular & Italic Bold"}),(0,h.jsx)(a.Z,{variant:"h6",children:"Line Height: 22px"})]})]})})]})})]})})}},77449:function(e,i,t){t.d(i,{Z:function(){return k}});var n=t(93433),r=t(29439),a=t(4942),o=t(63366),s=t(87462),l=t(47313),d=t(83061),c=t(21921),h=t(28170),u=t(64164),m=t(11236),x=t(45730),g=t(2995),Z=t(42669),p=t(77430),j=t(32298);function v(e){return(0,j.Z)("MuiLink",e)}var b=(0,p.Z)("MuiLink",["root","underlineNone","underlineHover","underlineAlways","button","focusVisible"]),f=t(46428),y=t(17551),S={primary:"primary.main",textPrimary:"text.primary",secondary:"secondary.main",textSecondary:"text.secondary",error:"error.main"},H=function(e){var i=e.theme,t=e.ownerState,n=function(e){return S[e]||e}(t.color),r=(0,f.D)(i,"palette.".concat(n),!1)||t.color,a=(0,f.D)(i,"palette.".concat(n,"Channel"));return"vars"in i&&a?"rgba(".concat(a," / 0.4)"):(0,y.Fq)(r,.4)},w=t(46417),L=["className","color","component","onBlur","onFocus","TypographyClasses","underline","variant","sx"],B=(0,u.ZP)(Z.Z,{name:"MuiLink",slot:"Root",overridesResolver:function(e,i){var t=e.ownerState;return[i.root,i["underline".concat((0,h.Z)(t.underline))],"button"===t.component&&i.button]}})((function(e){var i=e.theme,t=e.ownerState;return(0,s.Z)({},"none"===t.underline&&{textDecoration:"none"},"hover"===t.underline&&{textDecoration:"none","&:hover":{textDecoration:"underline"}},"always"===t.underline&&(0,s.Z)({textDecoration:"underline"},"inherit"!==t.color&&{textDecorationColor:H({theme:i,ownerState:t})},{"&:hover":{textDecorationColor:"inherit"}}),"button"===t.component&&(0,a.Z)({position:"relative",WebkitTapHighlightColor:"transparent",backgroundColor:"transparent",outline:0,border:0,margin:0,borderRadius:0,padding:0,cursor:"pointer",userSelect:"none",verticalAlign:"middle",MozAppearance:"none",WebkitAppearance:"none","&::-moz-focus-inner":{borderStyle:"none"}},"&.".concat(b.focusVisible),{outline:"auto"}))})),k=l.forwardRef((function(e,i){var t=(0,m.Z)({props:e,name:"MuiLink"}),a=t.className,u=t.color,Z=void 0===u?"primary":u,p=t.component,j=void 0===p?"a":p,b=t.onBlur,f=t.onFocus,y=t.TypographyClasses,H=t.underline,k=void 0===H?"always":H,C=t.variant,R=void 0===C?"inherit":C,F=t.sx,q=(0,o.Z)(t,L),W=(0,x.Z)(),z=W.isFocusVisibleRef,M=W.onBlur,P=W.onFocus,A=W.ref,T=l.useState(!1),D=(0,r.Z)(T,2),N=D[0],V=D[1],_=(0,g.Z)(i,A),X=(0,s.Z)({},t,{color:Z,component:j,focusVisible:N,underline:k,variant:R}),I=function(e){var i=e.classes,t=e.component,n=e.focusVisible,r=e.underline,a={root:["root","underline".concat((0,h.Z)(r)),"button"===t&&"button",n&&"focusVisible"]};return(0,c.Z)(a,v,i)}(X);return(0,w.jsx)(B,(0,s.Z)({color:Z,className:(0,d.Z)(I.root,a),classes:y,component:j,onBlur:function(e){M(e),!1===z.current&&V(!1),b&&b(e)},onFocus:function(e){P(e),!0===z.current&&V(!0),f&&f(e)},ref:_,ownerState:X,variant:R,sx:[].concat((0,n.Z)(Object.keys(S).includes(Z)?[]:[{color:Z}]),(0,n.Z)(Array.isArray(F)?F:[F]))},q))}))}}]);