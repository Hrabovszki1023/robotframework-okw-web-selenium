# Schlüsselwörter: Ignore-Regel

Für bestimmte Schlüsselwörter lässt sich die Ausführung überspringen, wenn kein sinnvoller Erwartungs- oder Eingabewert vorliegt. OKW4Robot unterstützt dafür eine generische Ignore-Regel.

- Empfohlenes Token: $IGNORE (Groß-/Kleinschreibung egal)
- Optional: Über ${OKW_IGNORE_EMPTY}=YES können auch leere Werte ("" bzw. nur Whitespaces) ignoriert werden.

Wichtig zu ${IGNORE} (mit geschweiften Klammern):
- ${IGNORE} ist eine Robot-Variable. Wenn sie nicht definiert ist, schlägt Robot mit “Variable '${IGNORE}' not found” fehl, bevor das Keyword aufgerufen wird.
- Wenn du ${IGNORE} verwenden möchtest, definiere sie in der Suite als Variable, die auf den Literal-String $IGNORE zeigt:

```robotframework
*** Variables ***
${IGNORE}    $IGNORE
```

Betroffene Schlüsselwörter (No-Op bei $IGNORE bzw. – falls aktiviert – bei leeren Werten):
- SetValue
- Select
- TypeKey
- VerifyValue, VerifyValueWCM, VerifyValueREGX

Sonderfall TypeKey (Löschen):
- Verwende das Literal $DELETE, um den Feldinhalt zu löschen (bevorzugt via Adapter clear_text, sonst CTRL+A + DELETE).
- Hinweis: ${DELETE} wäre eine Variable; wenn sie nicht definiert ist, schlägt Robot fehl. Daher $DELETE verwenden.

Beispiele (Robot Framework):
```robotframework
SetValue         NameDesWidgets     $IGNORE     # Kein Setzen
Select           Combo               $IGNORE     # Keine Auswahl
TypeKey          Eingabe             $DELETE     # Inhalt löschen
VerifyValue      Label               $IGNORE     # Keine Prüfung
# Optional (wenn ${OKW_IGNORE_EMPTY}=YES gesetzt ist):
VerifyValueWCM   Label               "   "      # Whitespaces -> Ignoriert
```

Leere-Werte-Semantik (${EMPTY}):
- ${EMPTY} ist ein Robot BuiltIn, das zu "" expandiert. Wenn ${OKW_IGNORE_EMPTY} auf NO (Standard) steht, kann damit gezielt auf leeren Text geprüft bzw. leer gesetzt werden.
- Wenn ${OKW_IGNORE_EMPTY}=YES genutzt wird, sind leere Werte global ignoriert. In diesem Modus bitte explizit mit Nicht-Leerwerten arbeiten oder das Ignorieren nur über $IGNORE steuern (oder ${IGNORE} wie oben definiert).

Hinweis: VerifyExist ist bewusst ausgenommen und erwartet weiterhin YES oder NO.
