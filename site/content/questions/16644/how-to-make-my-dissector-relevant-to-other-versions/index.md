+++
type = "question"
title = "How to make my dissector relevant to other versions"
description = '''Hey, I built a dissector for my WireShark version (after doing all that steps of installing cygwin etc. for building WireShark). Now, my dissector works only on my build of WireShark (ver 1.9 ... ), and not on, lets say, the newest WireShark version 1.8.4 that I can download from www.wireshark.org. ...'''
date = "2012-12-06T10:26:00Z"
lastmod = "2012-12-06T11:06:00Z"
weight = 16644
keywords = [ "dissector", "wireshark" ]
aliases = [ "/questions/16644" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to make my dissector relevant to other versions](/questions/16644/how-to-make-my-dissector-relevant-to-other-versions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16644-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey, I built a dissector for my WireShark version (after doing all that steps of installing cygwin etc. for building WireShark). Now, my dissector works only on my build of WireShark (ver 1.9 ... ), and not on, lets say, the newest WireShark version 1.8.4 that I can download from <a href="http://www.wireshark.org">www.wireshark.org</a>.</p><p>I saw that it is possible to create an installer of my version, which I can spread, and then my dissector will also work for others...</p><p>But I wanted to ask if it possible some how, by changing the version some where, to make my dissector relevant for other/older versions of WireShark which are official releases.</p><p>Thanks ahead.</p><p>edit: I tried downloading 1.8 source, building it, then building my dissector... but the official 1.8 release doesn't recognize it:</p><p>"Couldn't load module C:\Program Files\Wireshark\plugins\1.8.3\mydissector.dll: `C:\Program Files\Wireshark\plugins\1.8.3\mydissector.dll': %1 is not a valid Win32 application."</p></div><div id="question-tags" class="tags-container tags">dissector wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Dec '12, 10:26</strong></p><img src="https://secure.gravatar.com/avatar/b7ccaef1113111fc5cb2bb2a0d866a4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hudac&#39;s gravatar image" /><p>hudac<br />
<span class="score" title="61 reputation points">61</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hudac has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Dec '12, 02:04</p></div></div><div id="comments-container-16644" class="comments-container"></div><div id="comment-tools-16644" class="comment-tools"></div><div class="clear"></div><div id="comment-16644-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16647"></span>

<div id="answer-container-16647" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16647-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>plugins are only guaranteed to work with the version of Wireshark they are compiled with as we haven't comitted to a stable API yet. If yo want your plugin to work with 1.8 you will have to download the 1.8 sources and complie your plugin against that version.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '12, 11:06</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-16647" class="comments-container"><span id="16649"></span><div id="comment-16649" class="comment"><div id="post-16649-score" class="comment-score"></div><div class="comment-text"><p>What is the most recent svn revision for 1.8 sources?</p></div><div id="comment-16649-info" class="comment-info"><span class="comment-age">(06 Dec '12, 11:18)</span> SidR</div></div><span id="16650"></span><div id="comment-16650" class="comment"><div id="post-16650-score" class="comment-score">1</div><div class="comment-text"><p>You can check it out from here I think <a href="http://anonsvn.wireshark.org/wireshark/trunk-1.8/">http://anonsvn.wireshark.org/wireshark/trunk-1.8/</a> or use a tarball of the latest release.</p></div><div id="comment-16650-info" class="comment-info"><span class="comment-age">(06 Dec '12, 11:22)</span> Anders ♦</div></div><span id="16652"></span><div id="comment-16652" class="comment"><div id="post-16652-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry for the ignorance but what is tarball ?</p></div><div id="comment-16652-info" class="comment-info"><span class="comment-age">(06 Dec '12, 11:39)</span> hudac</div></div><span id="16731"></span><div id="comment-16731" class="comment"><div id="post-16731-score" class="comment-score"></div><div class="comment-text"><p>Hey, I tried it and it didn't work. I downloaded 1.8 source and built it, then built my dissector... but the official 1.8 release doesn't recognize it:</p><p>"Couldn't load module C:\Program Files\Wireshark\plugins\1.8.3\mydissector.dll: `C:\Program Files\Wireshark\plugins\1.8.3\mydissector.dll': %1 is not a valid Win32 application."</p></div><div id="comment-16731-info" class="comment-info"><span class="comment-age">(09 Dec '12, 00:18)</span> hudac</div></div></div><div id="comment-tools-16647" class="comment-tools"></div><div class="clear"></div><div id="comment-16647-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

