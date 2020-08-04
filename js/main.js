import React from 'react';
import ReactDOM from 'react-dom';
import ExampleWork from './example-work';

   {
     'title': "Work Example",
     'image': {
       'desc': "example screenshot of a project involving cats",
       'src': "images/example3.png",
       'comment': `"Bengal cat" by roberto shabs is licensed under CC BY
                   https://www.flickr.com/photos/37287295@N00/2540855181`
     }
   }
 ]

 ReactDOM.render(<ExampleWork work={myWork}/>, document.getElementById('example-work'));
}
