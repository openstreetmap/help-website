+++
type = "question"
title = "How to install wireshark in linux to support lua?"
description = '''Hi All, I want to use wireshark in linux to parse self-define protocol. So I write a lua plugin. Bug I am not sure if wireshark in linux can support lua. I download wireshark-1.5.0.tar.bz2,  tar -xvjf wireshark-1.5.0.tar.bz2 cd wireshark-1.5.0 ./configure but i got following message: Install dumpcap...'''
date = "2013-12-31T23:30:00Z"
lastmod = "2014-01-01T12:38:00Z"
weight = 28507
keywords = [ "lua", "linux", "wireshark" ]
aliases = [ "/questions/28507" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to install wireshark in linux to support lua?](/questions/28507/how-to-install-wireshark-in-linux-to-support-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28507-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I want to use wireshark in linux to parse self-define protocol. So I write a lua plugin. Bug I am not sure if wireshark in linux can support lua.</p><p>I download wireshark-1.5.0.tar.bz2,<br />
</p><p>tar -xvjf wireshark-1.5.0.tar.bz2<br />
cd wireshark-1.5.0<br />
./configure<br />
but i got following message:<br />
Install dumpcap with capabilities : no<br />
Install dumpcap setuid : no<br />
Use dumpcap group : (none)<br />
Use plugins : yes<br />
Use lua library : no<br />
It can't support lua?I install lua and lua-devel.<br />
cd lua-5.2.0<br />
make linux<br />
make install<br />
yum install lua-devel<br />
</p><p>So I configure wireshark as following:<br />
./configure --with-lua=/usr/local/etc<br />
I got following errors:<br />
checking for luaL_register in -llua... no<br />
checking for luaL_register in -llua5.1... no<br />
configure: error: Linking with liblua failed.<br />
</p><p>Could you please tell me how to install wireshark in linux? My linux release is Fedora 13.<br />
</p><p>Thank you very much.<br />
</p><p>Rong</p></div><div id="question-tags" class="tags-container tags">lua linux wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Dec '13, 23:30</strong></p><img src="https://secure.gravatar.com/avatar/135b8a0148326af62a77a4bbeb96ea9e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rong&#39;s gravatar image" /><p>Rong<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rong has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-28507" class="comments-container"></div><div id="comment-tools-28507" class="comment-tools"></div><div class="clear"></div><div id="comment-28507-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28512"></span>

<div id="answer-container-28512" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28512-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I install lua and lua-devel.</p></blockquote><pre><code>cd lua-5.2.0
make linux
make install
yum install lua-devel</code></pre><p>So why did you install Lua "by hand" and install the Lua development package with "yum install"? Try either using "yum install" to install Lua, or doing whatever is necessary in the lua-5.2.0 directory to install the development stuff (header files and libraries).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jan '14, 12:38</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Jan '14, 12:38</p></div></div><div id="comments-container-28512" class="comments-container"><span id="28514"></span><div id="comment-28514" class="comment"><div id="post-28514-score" class="comment-score"></div><div class="comment-text"><p>Isn't Fedora 13 and Wireshark 1.5 somewhat old? In the case of Wireshark 1.5 that's a development release anyway so maybe not the best version to be working with.</p></div><div id="comment-28514-info" class="comment-info"><span class="comment-age">(01 Jan '14, 15:32)</span> grahamb ♦</div></div></div><div id="comment-tools-28512" class="comment-tools"></div><div class="clear"></div><div id="comment-28512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

