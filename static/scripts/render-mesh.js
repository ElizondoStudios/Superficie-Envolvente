function renderMesh(){
    // creamos la escena
    const scene = new THREE.Scene();
    
    // añadimos una cámara para ver al modelo
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth/2/window.innerHeight, 0.1, 1000);
    camera.position.z = 5;
    
    // inicializamos el renderer
    const canvas = document.getElementById('canvas-mesh');
    const renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true });
    renderer.setSize(window.innerWidth/2, window.innerHeight);
    document.body.appendChild(renderer.domElement);
    
    const controls = new THREE.OrbitControls(camera, renderer.domElement);
    
    // añadimos luces para que se pueda ver el modelo
    scene.add(new THREE.AmbientLight(0x404040));
    
    // añadimos una luz que apunte al modelo desde arriba para que se note el 3D y la superficie
    const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
    directionalLight.position.set(5, 5, 5).normalize();
    scene.add(directionalLight);
    
    // cargamos el modelo
    const loader = new THREE.OBJLoader();
        loader.load(window.meshUrl, function (object) {
        object.scale.set(0.05, 0.05, 0.05); 
        object.position.set(0, -1, 0);
        scene.add(object);
    }, xhr => {
        console.log((xhr.loaded / xhr.total * 100) + '% loaded');
    }, err => {
        console.error('Error loading model', err);
    });
    
    function animate() {
        requestAnimationFrame(animate);
        renderer.render(scene, camera);
    }
    
    animate();
}

renderMesh()