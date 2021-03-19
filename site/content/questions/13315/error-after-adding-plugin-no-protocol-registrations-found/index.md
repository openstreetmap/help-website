+++
type = "question"
title = "Error after adding Plugin: No protocol registrations found"
description = '''Hello.  I&#x27;m writing a postdissector plugin in C to look into the options field found in the tcp header. Unfortunately, the following error turns up when I try to build:  Making plugin.c (using python) No protocol registrations found NMAKE : fatal error U1077: &#x27;C:&#92;Python27&#92;python.exe&#x27; : return code &#x27;...'''
date = "2012-08-02T06:27:00Z"
lastmod = "2012-08-02T22:27:00Z"
weight = 13315
keywords = [ "u1077", "errors", "build", "plugins" ]
aliases = [ "/questions/13315" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Error after adding Plugin: No protocol registrations found](/questions/13315/error-after-adding-plugin-no-protocol-registrations-found)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13315-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello. I'm writing a postdissector plugin in C to look into the options field found in the tcp header. Unfortunately, the following error turns up when I try to build:<br />
</p><p>Making plugin.c (using python)<br />
No protocol registrations found<br />
NMAKE : fatal error U1077: 'C:\Python27\python.exe' : return code '0x1'<br />
Stop.<br />
NMAKE : fatal error U1077: '"c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe"' : return code '0x2'<br />
Stop.<br />
NMAKE : fatal error U1077: '"c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe"' : return code '0x2'<br />
Stop.<br />
NMAKE : fatal error U1077: '"c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe"' : return code '0x2'<br />
Stop.<br />
</p><p>It was building fine before I added the plugin and made changes as specified in README.plugins.<br />
Could anyone please tell me what the problem could be?!!</p><p>Edit: I found out in another thread that the problem should be in my config.nmake file. However, I followed the instructions in the Win32 Step-by-Step Setup Guide carefully. I'm building this on a 64 bit Windows 7 system. Why does it still not build?</p></div><div id="question-tags" class="tags-container tags">u1077 errors build plugins</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '12, 06:27</strong></p><img src="https://secure.gravatar.com/avatar/46196bc495ce51058590c4e4ae334d22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SidR&#39;s gravatar image" /><p>SidR<br />
<span class="score" title="245 reputation points">245</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SidR has 3 accepted answers">30%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Aug '12, 21:46</p></div></div><div id="comments-container-13315" class="comments-container"><span id="13334"></span><div id="comment-13334" class="comment"><div id="post-13334-score" class="comment-score">1</div><div class="comment-text"><p>I would guess the script are looking for something like this void proto_register_foo(void) { : }</p><p>and void proto_reg_handoff_foo(void) { : }</p><p>Do you have similar code in your plugin?</p></div><div id="comment-13334-info" class="comment-info"><span class="comment-age">(02 Aug '12, 22:01)</span> Anders ♦</div></div><span id="13335"></span><div id="comment-13335" class="comment"><div id="post-13335-score" class="comment-score"></div><div class="comment-text"><p>That seems to be the problem.<br />
Looks I have written it as void protocol_register_foo(void) instead of void proto_register_foo(). Thank you so much Anders!</p></div><div id="comment-13335-info" class="comment-info"><span class="comment-age">(02 Aug '12, 22:20)</span> SidR</div></div></div><div id="comment-tools-13315" class="comment-tools"></div><div class="clear"></div><div id="comment-13315-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13336"></span>

<div id="answer-container-13336" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13336-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I would guess the script are looking for something like this void proto_register_foo(void) { : }</p><p>and void proto_reg_handoff_foo(void) { : }</p><p>Do you have similar code in your plugin?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Aug '12, 22:27</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span> </br></br></p></div></div><div id="comments-container-13336" class="comments-container"></div><div id="comment-tools-13336" class="comment-tools"></div><div class="clear"></div><div id="comment-13336-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

