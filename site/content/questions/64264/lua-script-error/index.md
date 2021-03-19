+++
type = "question"
title = "lua script error"
description = '''Recently I encountered a problem. I wrote a lua script and it can work normally on Win7-64bit PC， but today I use it on Win10-64bit PC，it pop up a error： 【Lua:error during loading xxx.lua:71 line :bad argument #3 to &#x27;bytes&#x27; (display must be either base.NONE,base.DOT,base.DASH,base.COLON.base.SPACE)】...'''
date = "2017-10-26T22:42:00Z"
lastmod = "2017-10-26T22:42:00Z"
weight = 64264
keywords = [ "lua" ]
aliases = [ "/questions/64264" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [lua script error](/questions/64264/lua-script-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64264-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Recently I encountered a problem. I wrote a lua script and it can work normally on Win7-64bit PC，</p><p>but today I use it on Win10-64bit PC，it pop up a error：</p><p>【Lua:error during loading xxx.lua:71 line :bad argument #3 to 'bytes' (display must be either base.NONE,base.DOT,base.DASH,base.COLON.base.SPACE)】</p><p>this lua script's Line 71 is shown as below</p><p>f_RawData = ProtoField.bytes("HdplcFrame.RawData", "Raw Data", base.HEX)</p><p>I would appreciate it very much if you would help me with it. Thanks in advance</p></div><div id="question-tags" class="tags-container tags">lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '17, 22:42</strong></p><img src="https://secure.gravatar.com/avatar/afe2cdb7c2fe1cc4547e072345a21bda?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hithall&#39;s gravatar image" /><p>hithall<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hithall has no accepted answers">0%</span></p></div></div><div id="comments-container-64264" class="comments-container"><span id="64271"></span><div id="comment-64271" class="comment"><div id="post-64271-score" class="comment-score"></div><div class="comment-text"><p>Wireshark versions on both platforms?</p></div><div id="comment-64271-info" class="comment-info"><span class="comment-age">(27 Oct '17, 01:49)</span> Jaap ♦</div></div><span id="64286"></span><div id="comment-64286" class="comment"><div id="post-64286-score" class="comment-score"></div><div class="comment-text"><p>Based on the error message, is it erroring out on "base.HEX"? Not sure what the factor is between Win7 and Win10 on base.HEX</p></div><div id="comment-64286-info" class="comment-info"><span class="comment-age">(27 Oct '17, 06:53)</span> Papa Packet</div></div><span id="64288"></span><div id="comment-64288" class="comment"><div id="post-64288-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/45887/papa-packet"></a><a href="https://ask.wireshark.org/users/45887/papa-packet">@Papa Packet</a>, that's exactly why <a href="https://ask.wireshark.org/users/4/jaap"></a><a href="https://ask.wireshark.org/users/4/jaap">@Jaap</a> was asking for Wireshark version on both OSes because direct relationship to OS would be weird. It is more likely that something like 2.1.x is running on Win7 and something like 2.4.x is running on Win10. Between these releases, the Lua API has become more strict in some aspects.</p></div><div id="comment-64288-info" class="comment-info"><span class="comment-age">(27 Oct '17, 07:14)</span> sindy</div></div></div><div id="comment-tools-64264" class="comment-tools"></div><div class="clear"></div><div id="comment-64264-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

