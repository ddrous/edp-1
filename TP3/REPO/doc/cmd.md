# Pour login ATLAS
`ssh nzoyemngueguin@atlas.math.unistra.fr`  
Password: 

# Pour configurer ATLAS en ssh
```
Host *
\# ServerAliveInterval 15
 ServerAliveCountMax 30
 ServerAliveInterval 600
 IPQoS=throughput
host atlas.math.unistra.fr
  user <login>
host atlas
 user <login>
 hostname atlas.math.unistra.fr
```

# Pour eviter de mettre le password tout le temps  
`mkdir .ssh`  
`chmod -R go-rwx .ssh`  
`$HOME/.ssh/config`  
`ssh-keygen`   
`cat .ssh/id_rsa.pub`   

Creer ou copie le contenu de $HOME/.bash_profile à partir des lignes ci-dessus   
```
SSHAGENT=/usr/bin/ssh-agent
SSHAGENTARGS="-s"
if [ -z "$SSH_AUTH_SOCK" -a -x "$SSHAGENT" ]; then
   eval `$SSHAGENT $SSHAGENTARGS`
  trap "kill $SSH_AGENT_PID" 0
fi
```
  
Ensuite:
`source .bash_profile`, `source $HOME/.bash_profile`

# Pour facilement aller sans id sous WINDOWS
```
host atlas.math.unistra.fr
  ForwardAgent Yes
  user prudhomm
host atlas
 ForwardAgent Yes
 user prudhomm
 hostname atlas.math.unistra.fr
```


# Pour cloner se placer dans toolbox pour la demo
`git clone https://github.com/feelpp/toolbox`

# Pour consulter les modules installes
`module avail`

# Pour charger les modules necessaires pour le TP
`module load feelpp-toolboxes/develop_gcc830_openmpi402`

# Pour se placer proche d'un fichier config disk.cfg
Une fois dans toolbox, 
`cd examples/modules/csm/examples/ribs ` ou pllus rapide encore   
`cd ../../../toolbox/examples/modules/csm/examples/ribs ` ou encore,    
`cd examples/modules/cfd/examples/pipestokes/case_corrections/dirichlet/2d`

# Pour executer le programme
`feelpp_toolbox_solid --config-file disk.cfg`

# Pour visualiser les donnees 
`cd ~/feel/toolboxes/solid/ribs/disk2/P2/np_1/solid.exports`   
Sous Windows: `C:\Users\Roussel\Dropbox\Unistra\SEMESTRE 2\EDP 1\Travaux Pratiques\TP3\DATA\feel\toolboxes\solid\ribs\disk2\P2\np_1\solid.exports`

# Pour synchroniser
Dans le repertoire courant
`rsync -avz nzoyemngueguin@atlas.math.unistra.fr:~/feel .`, ou plus simplement
`rsync -avz nzoyemngueguin@atlas.math.unistra.fr:~/feel "/mnt/c/Users/Roussel/Dropbox/Unistra/SEMESTRE 2/EDP 1/Travaux Pratiques/TP3/DATA"`   
Mot de passe: 


# Documentation
assurez vous que tout fonctionne via vscode   
lisez [http://docs.feelpp.org/toolboxes/0.108/csm/toolbox/]   
lisez [http://docs.feelpp.org/toolboxes/0.108/cfd/toolbox/]   
regardez les exemples(voire en tester qquns): [http://docs.feelpp.org/cases/   0.108/csm/README/]   
regardez les exemples(voire en tester qquns): [http://docs.feelpp.org/cases/   0.108/cfd/README/]  



# Comment lancer l'agent SSH
###sous linux: 
`eval $(ssh-agent -s)`     
`ssh-add ~/.ssh/id_rsa`

###sous Windows: 

# Setup pour le TP3
### Sous Windows
- lancer le VPN
- lancer VS Code

### Sous le WSL
- lancer l'agent SSH
- `cd "/mnt/c/Users/Roussel/Dropbox/Unistra/SEMESTRE 2/EDP 1/Travaux Pratiques/TP3/tp3-fluid-solid"`
- `rsync -avz nzoyemngueguin@atlas.math.unistra.fr:~/edp-tp3/data .`

### Sous ATLAS
- lancer l'agent SSH
- `module load feelpp-toolboxes/develop_gcc830_openmpi402`
- `cd data`
- `export FEELPP_REPOSITORY=$PWD`
- `cd ..`
- `mpirun -np 4 feelpp_toolbox_fluid --config-file navier_stokes.cfg`
