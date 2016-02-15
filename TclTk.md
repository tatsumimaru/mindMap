Tcl/Tk（ティクル・ティーケー）は、スクリプト言語 Tcl と、その GUIツールキット Tk を指す。非常に強力な GUI ツールキットと、シンプルな文法をもつ言語により、GUI ツールを素早く作り上げるのに適した強力なスクリプティング環境である。

現在、各種オペレーティングシステム（UNIX、Windows、Macintosh）上で動作する。
Tcl 言語は、コマンド行のみで構造化文法をフォローしてしまう非常にシンプルな文法を特徴とする。Tk はクロスプラットフォームな GUI 環境としても有名で、Tcl 言語に限らず、Perl、Python、Ruby などの言語環境からも利用できる。
他にも ウェブブラウザ上で Tcl/Tk を動作させるプラグイン Tclet（ティクレット） がある。
Tcl がカリフォルニア大学バークレー校のジョン・ケネス・オースターハウト博士[3]により最初に開発されたのは1988年の事である。

Tk は Tcl 用に開発された、非常に簡単なコードで GUI を作成できるツールキットである。1990年代初頭に Tcl にバンドルされる形で公開された。

Tcl は当初の設計意図と異なり、アプリケーションの組み込み言語として使われるよりも、Tk と合わせた「Tcl/Tk」の形の GUI スクリプティング環境として人気を博した。特に Tk の人気は高く、Tcl にとどまらず Perl（Perl/Tk）、Python （Tkinter）、Ruby （Ruby/Tk）など、他の言語でも標準的な GUI キットとして Tk が利用された。

オースターハウトがサン・マイクロシステムズに勤めていた1994-1998年は Tcl/Tk は同社で開発が進められた。
オースターハウトの退職に伴い、Tcl/Tk の開発はサンの手を離れた。2000年からは Tcl/Tk の開発はオープンソースにその場を移し、精力的に開発が続けられている。
2005年現在 Tcl 言語は「Tcl/Tk」の知名度とは裏腹に利用者数は少なく、Perl や Python、Ruby に比べ劣勢と言わざるを得ない。特に日本国内での利用者数は少ない。ただし、EDAツールにおいては標準的なスクリプト言語として広く利用されているほか、電子国土Webシステムにおいても一部で Tcl 言語が使われている。一方 Tk は、後発の GTK+、Qt と並び、軽量プログラミング言語における事実上の標準 GUI ツールキットの一つとなっており、広く利用されている。
なお、Tcl 言語の名前は「ツールコマンド言語」を意味する英語「tool command language」に由来し、Tk の名前は「ツールキット」を意味する英語「toolkit」に由来する。




#which tcl: returns nothing
#Git Project uses tcl for GUI.
#/usr/bin/tclsh
```
tatsumi@tatsumi-ubuntu:~/document$ tclsh
% q
invalid command name "q"
% quit
invalid command name "quit"
% exit
```
#/usr/lib/tcltk
```
tatsumi@tatsumi-ubuntu:~/document$ vi /usr/lib/tcltk/x86_64-linux-gnu/tk8.6/pkgIndex.tcl
```
```
if {[catch {package present Tcl 8.6.0}]} return
package ifneeded Tk 8.6.1 [list load [file normalize [file join /usr/lib/x86_64-linux-gnu libtk8.6.so]] Tk]
```
