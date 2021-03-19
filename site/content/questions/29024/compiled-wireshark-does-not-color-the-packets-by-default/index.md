+++
type = "question"
title = "Compiled wireshark does not color the packets by default"
description = '''After compiling Wireshark on my own on Ubuntu 13.10 (x64) with following configure script :   ./configure --prefix=/home/user/Downloads/wireshark-1.10.5/build_dir --with-adns --with-pcap --with-lua --with-libsmi --with-c-ares --with-portaudio --enable-setcap-install --enable-setuid-install --with-gt...'''
date = "2014-01-19T17:06:00Z"
lastmod = "2014-01-19T17:06:00Z"
weight = 29024
keywords = [ "compile", "coloring", "linux" ]
aliases = [ "/questions/29024" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Compiled wireshark does not color the packets by default](/questions/29024/compiled-wireshark-does-not-color-the-packets-by-default)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29024-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>After compiling Wireshark on my own on Ubuntu 13.10 (x64) with following <code>configure</code> script :</p><hr /><pre><code>./configure --prefix=/home/user/Downloads/wireshark-1.10.5/build_dir --with-adns --with-pcap --with-lua --with-libsmi  --with-c-ares  --with-portaudio --enable-setcap-install   --enable-setuid-install  --with-gtk3 --with-ssl</code></pre><hr /><pre><code>The Wireshark package has been configured with the following options.
                    Build wireshark : yes (with GTK+ 3)
                       Build tshark : yes
                     Build capinfos : yes
                      Build editcap : yes
                      Build dumpcap : yes
                     Build mergecap : yes
                   Build reordercap : yes
                    Build text2pcap : yes
                      Build randpkt : yes
                       Build dftest : yes
                     Build rawshark : yes

   Save files as pcap-ng by default : yes
  Install dumpcap with capabilities : yes
             Install dumpcap setuid : no
                  Use dumpcap group : (none)
                        Use plugins : yes
                    Use Lua library : yes
                 Use Python binding : no
                   Build rtp_player : yes
             Build profile binaries : no
                   Use pcap library : yes
                   Use zlib library : yes
               Use kerberos library : yes (MIT)
                 Use c-ares library : yes
               Use GNU ADNS library : no (using c-ares instead)
                Use SMI MIB library : yes
             Use GNU crypto library : yes
             Use SSL crypto library : yes
           Use IPv6 name resolution : yes
                 Use gnutls library : yes
     Use POSIX capabilities library : yes
                  Use GeoIP library : no
                     Use nl library : no</code></pre><p>Yet when installed from package manager it does color the packets by default. Am I missing something ?</p></div><div id="question-tags" class="tags-container tags">compile coloring linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jan '14, 17:06</strong></p><img src="https://secure.gravatar.com/avatar/3aaa7d9ab52fa2be477f1df7ca99a6a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Patryk&#39;s gravatar image" /><p>Patryk<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Patryk has no accepted answers">0%</span></p></div></div><div id="comments-container-29024" class="comments-container"><span id="29057"></span><div id="comment-29057" class="comment"><div id="post-29057-score" class="comment-score"></div><div class="comment-text"><p>is that exactly the same version of Wireshark in the Ubuntu repository?</p></div><div id="comment-29057-info" class="comment-info"><span class="comment-age">(21 Jan '14, 05:07)</span> Kurt Knochner ♦</div></div><span id="29059"></span><div id="comment-29059" class="comment"><div id="post-29059-score" class="comment-score"></div><div class="comment-text"><p>I have downloaded the source code from Wireshark website and compiled it by myself. The problem has been solved by exporting the color themes from the other version and importing them to the compiled one (apparently the compiled version does not have the color themes by default).</p></div><div id="comment-29059-info" class="comment-info"><span class="comment-age">(21 Jan '14, 05:29)</span> Patryk</div></div><span id="29072"></span><div id="comment-29072" class="comment"><div id="post-29072-score" class="comment-score"></div><div class="comment-text"><p>did you run Wireshark from the compile directory, or did you run 'make install' before starting Wireshark?</p></div><div id="comment-29072-info" class="comment-info"><span class="comment-age">(21 Jan '14, 11:56)</span> Kurt Knochner ♦</div></div><span id="29073"></span><div id="comment-29073" class="comment"><div id="post-29073-score" class="comment-score"></div><div class="comment-text"><p>I've tried both.</p></div><div id="comment-29073-info" class="comment-info"><span class="comment-age">(21 Jan '14, 11:57)</span> Patryk</div></div></div><div id="comment-tools-29024" class="comment-tools"></div><div class="clear"></div><div id="comment-29024-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

