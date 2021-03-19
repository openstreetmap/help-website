+++
type = "question"
title = "Openflow v1,v2 and v3 support for wireshark"
description = '''Hi, I tried to build wireshark 1.12 from source by downloading tar file on ubuntu 12.0.4. After doing $sudo make install when I type $wireshark it says command not found. Then I tried $sudo apt-get install wireshark. It installed wireshark 1.11.1 version. In that I could find only OpenFlow V4 in the...'''
date = "2015-01-10T00:29:00Z"
lastmod = "2015-01-10T00:29:00Z"
weight = 39015
keywords = [ "openflow" ]
aliases = [ "/questions/39015" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Openflow v1,v2 and v3 support for wireshark](/questions/39015/openflow-v1v2-and-v3-support-for-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39015-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I tried to build wireshark 1.12 from source by downloading tar file on ubuntu 12.0.4. After doing $sudo make install when I type $wireshark it says command not found. Then I tried $sudo apt-get install wireshark. It installed wireshark 1.11.1 version. In that I could find only OpenFlow V4 in the support protocol list.</p><p>I need to enable support for Openflow v1,v2 and v3</p><p>Please help me to fix it.</p><p>Thanks, Kokila</p></div><div id="question-tags" class="tags-container tags">openflow</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jan '15, 00:29</strong></p><img src="https://secure.gravatar.com/avatar/63c9ebcf5f89282fb1c71881239efa08?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kokila&#39;s gravatar image" /><p>kokila<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kokila has no accepted answers">0%</span></p></div></div><div id="comments-container-39015" class="comments-container"><span id="39018"></span><div id="comment-39018" class="comment"><div id="post-39018-score" class="comment-score"></div><div class="comment-text"><blockquote><p>when I type $wireshark it says command not found.</p></blockquote><p>Why do you try to run $wireshark? That would be a variable ($) in your shell.</p></div><div id="comment-39018-info" class="comment-info"><span class="comment-age">(10 Jan '15, 04:37)</span> Kurt Knochner ♦</div></div><span id="39067"></span><div id="comment-39067" class="comment"><div id="post-39067-score" class="comment-score"></div><div class="comment-text"><p>I have entered wireshark only. I have included $ to intimate that I am running from shell.</p></div><div id="comment-39067-info" class="comment-info"><span class="comment-age">(11 Jan '15, 19:41)</span> kokila</div></div><span id="39068"></span><div id="comment-39068" class="comment"><div id="post-39068-score" class="comment-score"></div><div class="comment-text"><p>Did "make" really finsih without any errors? What happens if you go to your build directory and type ./wireshark or ./wireshark-gtk?</p><p>Openflow V1,V4 and v5 are supported by Wireshark development version. V1 support may be incomplete. I'm not sure of the status in 1.12.x</p><p>An external plugin can be found here <a href="http://archive.openflow.org/wk/index.php/OpenFlow_Wireshark_Dissector">http://archive.openflow.org/wk/index.php/OpenFlow_Wireshark_Dissector</a></p></div><div id="comment-39068-info" class="comment-info"><span class="comment-age">(12 Jan '15, 00:50)</span> Anders ♦</div></div><span id="39069"></span><div id="comment-39069" class="comment"><div id="post-39069-score" class="comment-score"></div><div class="comment-text"><p>wireshark.desktop and wireshark.pc.in are the only files available in build directory. the output of make is given below.</p><p>make[2]: Entering directory <code>/home/kokila/Desktop/kokila/wireshark-1.12.2/ui/qt'   UIC      ui_about_dialog.h /bin/bash: /usr/lib/qt4:/usr/share/qt4:: No such file or directory make[2]: *** [ui_about_dialog.h] Error 127 make[2]: Leaving directory</code>/home/kokila/Desktop/kokila/wireshark-1.12.2/ui/qt' make[1]: <strong><em>[all-recursive] Error 1 make[1]: Leaving directory `/home/kokila/Desktop/kokila/wireshark-1.12.2' make:</em></strong> [all] Error 2</p></div><div id="comment-39069-info" class="comment-info"><span class="comment-age">(12 Jan '15, 01:07)</span> kokila</div></div><span id="39074"></span><div id="comment-39074" class="comment"><div id="post-39074-score" class="comment-score"></div><div class="comment-text"><p>Seems like you don't have all the build dependencies for wireshark loaded and/or not giving the right input to ./configure.</p><p>This is what I use:</p><p><code> sudo apt-get build-dep wireshark sudo apt-get install qt5-default sudo apt-get install libssl-dev sudo apt-get install libgtk-3-dev</code></p><p><code></code></p><p><code>./autogen.sh ./configure --with-ssl --enable-setcap-install</code></p></div><div id="comment-39074-info" class="comment-info"><span class="comment-age">(12 Jan '15, 04:02)</span> Anders ♦</div></div></div><div id="comment-tools-39015" class="comment-tools"></div><div class="clear"></div><div id="comment-39015-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

