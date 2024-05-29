### Git credential storage

- (Windows) In order to make Git recognize your SSH configs, I faced a problem where you need to tell Git explicitely to use the internal OpenSSH instead of its own:  

```
git config --global core.sshCommand C:/Windows/System32/OpenSSH/ssh.exe
```
