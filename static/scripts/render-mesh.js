function renderMesh() {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth/2/window.innerHeight, 0.1, 1000);
    camera.position.z = 4;
  
    const canvas = document.getElementById('canvas-mesh');
    const renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true });
    renderer.setSize(window.innerWidth/2, window.innerHeight);
    document.body.appendChild(renderer.domElement);
  
    const controls = new THREE.OrbitControls(camera, renderer.domElement);
  
    scene.add(new THREE.AmbientLight(0x404040));
    const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
    directionalLight.position.set(5, 5, 5).normalize();
    scene.add(directionalLight);
  
    // Detecta la extensión del archivo
    const fileExtension = window.meshUrl.split('.').pop().toLowerCase();
  
    if (fileExtension === 'obj') {
      const loader = new THREE.OBJLoader();
      loader.load(window.meshUrl, function (object) {
        //Escala para que se vea mejor
        geometry.computeBoundingBox();

        const size = new THREE.Vector3();
        geometry.boundingBox.getSize(size);
        const maxSize = Math.max(size.x, size.y, size.z);
        const scaleFactor = 1.5 / maxSize;
        mesh.scale.set(scaleFactor, scaleFactor, scaleFactor);

        object.position.set(0, -1, 0);
        scene.add(object);
      }, xhr => {
        console.log((xhr.loaded / xhr.total * 100) + '% loaded');
      }, err => {
        console.error('Error loading OBJ model', err);
      });
  
    } else if (fileExtension === 'ply') {
      const loader = new THREE.PLYLoader();
      loader.load(window.meshUrl, function (geometry) {
        geometry.computeVertexNormals();
        const material = new THREE.MeshStandardMaterial({ color: 0xffffff, flatShading: true });
        const mesh = new THREE.Mesh(geometry, material);

        //Escala para que se vea mejor
        geometry.computeBoundingBox();

        const size = new THREE.Vector3();
        geometry.boundingBox.getSize(size);
        const maxSize = Math.max(size.x, size.y, size.z);
        const scaleFactor = 1.5 / maxSize;
        mesh.scale.set(scaleFactor, scaleFactor, scaleFactor);

        mesh.position.set(0, -1, 0);
        scene.add(mesh);
      }, xhr => {
        console.log((xhr.loaded / xhr.total * 100) + '% loaded');
      }, err => {
        console.error('Error loading PLY model', err);
      });
    } else {
      console.error('Unsupported file format:', fileExtension);
    }
  
    function animate() {
      requestAnimationFrame(animate);
      renderer.render(scene, camera);
    }
  
    animate();
  }
  
renderMesh();
  