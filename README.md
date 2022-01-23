# EIP Keylogger Proof of Concept
Proof of concept of a keylogger for cibersecurity educational purposes only <a href="https://eiposgrados.com/programas/master-en-ciberseguridad/">@eiposgrados</a>.

When starting the script, five options and a selector will appear:
```
EIP KeyLogger Options

==> Record Key                 (press ESC to back)
    Read Logs                  (press ANY KEY to back)
    Read Credentials           (press ANY KEY to back)
    Regenerate Credentials     (press ANY KEY to back)
    Exit
```
> Record Key: It will start a listener to intercept keys pressed.

> Read Logs: It will display the logs of keys pressed.

> Read Credentials: It will show the passwords obtained after detecting a domain (.com, .es, .eiposgrados.edu.es).

> Regenerate Credentials: It will regenerate the passwords if another application has been used to collect the logs.

> Exit: Exit the script.
