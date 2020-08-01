#Pour lancer Docker
WIN: 	`docker run --rm --name tp_edp -it -v $HOME/Dropbox/Unistra/SOURCE_CODE/edp1/tp0:/feel feelpp/feelpp`     
`docker run --rm -it -v ${PWD}:/feel feelpp/feelpp`         
LINUX:	`docker run --rm -it -v $HOME/csmi:/feel feelpp/feelpp` 

#Pour exécuter une commande en tant qu'admin
	`docker exec -u 0 -it tp_edp bash`

#Pour retourner au bash
	CTRL+P followed by CTRL+Q

#Commandes pour les permissions
LINUX:	`$HOME/csmi; chmod -R a+w csmi`

#Créer la géométrie avec Gmsh
`gmsh -2 -o triangle.msh /usr/share/feelpp/data/testcases/quickstart/laplacian/triangle/triangle.geo`

#Créer un problème dans Feel++
`feelpp_qs_laplacian_2d --config-file /usr/share/feelpp/data/testcases/quickstart/laplacian/triangle/triangle.cfg`

#Forcer une solution particulière
`feelpp_qs_laplacian_2d --config-file /usr/share/feelpp/data/testcases/quickstart/laplacian/triangle/triangle.cfg --gmsh.hsize=0.05 --checker.solution="x*x+cos(y)*y:x:y"`

#Exécuter sur 4 processeurs
`mpirun -np 4 feelpp_qs_laplacian_2d --config-file /usr/share/feelpp/data/testcases/quickstart/laplacian/triangle/triangle.cfg --gmsh.hsize=0.05 --checker.solution="x*x+cos(y)*y:x:y"`

#Si problème de nombre de processus,
`mpirun --use-hwthread-cpus -np 4 ...` 
Use this When the requested number of slots is larger than the number of CPUs but less than or equal to the number of hardware threads, `--use-hwthread-cpus` tells Open MPI's mapper to use HW threads as the mapping unit, not cores.

#En changeant les conditions au bord
`mpirun -np 4 feelpp_qs_laplacian_2d --config-file /usr/share/feelpp/data/testcases/quickstart/laplacian/triangle/triangle.cfg --gmsh.hsize=0.025 --checker.solution="x*x+cos(y)*y:x:y" --checker.check=false --f="sin(x)*cos(y):x:y" --g=0 --un=0 --r_2=0`

#Verification de la solution par ksp-rtol
`feelpp_qs_laplacian_2d --config-file triangle.cfg --ksp-monitor=1 --f=1 --checker.check=false --un=1 --g=0 --pc-type=none --ksp-type=cg --ksp-rtol=1e-10`

#Avec un fichier nouveau fichier geo
`feelpp_qs_laplacian_2d --config-file triangle.cfg --ksp-monitor=1 --f=1 --checker.check=false --un=1 --g=0 --pc-type=gamg --ksp-type=gmres --ksp-rtol=1e-10 --gmsh.hsize 0.0125 --gmsh.filename "$cfgdir/omega.geo" --r_2=0` 
ou encore
`..... --gmsh.filename "/feel/tp1/omega.geo"`

#Pour copier les fichiers geo/smh
`cp /usr/share/feelpp/data/testcases/quickstart/laplacian/triangle/triangle.geo .`

