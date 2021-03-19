+++
type = "question"
title = "How to &quot;Compile the dissector to a DLL or shared library&quot;?"
description = '''I have successfully built Wireshark from source code using the instructions in section 2.2 of the developers guide(win64 setup). I am now trying to build my dissector using the instructions in section 9.2. At the end of Section 9.2.1 it says, &quot;Compile the dissector to a DLL or shared library ...&quot;. C...'''
date = "2016-03-24T12:10:00Z"
lastmod = "2016-03-24T15:51:00Z"
weight = 51161
keywords = [ "win64", "dissector", "build" ]
aliases = [ "/questions/51161" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to "Compile the dissector to a DLL or shared library"?](/questions/51161/how-to-compile-the-dissector-to-a-dll-or-shared-library)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51161-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have successfully built Wireshark from source code using the instructions in section 2.2 of the developers guide(win64 setup). I am now trying to build my dissector using the instructions in section 9.2. At the end of Section 9.2.1 it says, "Compile the dissector to a DLL or shared library ...". Can someone tell me how to do this?</p><p>I found some old examples online, but they are not working. Do I use the "msbuild" command, as in section 2.2.12?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">win64 dissector build</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Mar '16, 12:10</strong></p><img src="https://secure.gravatar.com/avatar/b3270ea804306e71984b713be60df166?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rbw006&#39;s gravatar image" /><p>rbw006<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rbw006 has no accepted answers">0%</span></p></div></div><div id="comments-container-51161" class="comments-container"></div><div id="comment-tools-51161" class="comment-tools"></div><div class="clear"></div><div id="comment-51161-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51164"></span>

<div id="answer-container-51164" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51164-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yep, just rebuild the whole solution again and it will all work, assuming you've made the correct changes. If you've created a plugin dissector you can just rebuild your plugin by substituting the path to the plugin project file on the msbuild command line, e.g.</p><pre><code>msbuild /m /p:Configuration=RelWithDebInfo plugins\myplugin\myplugin.vcxproj</code></pre><p>You must have previously built Wireshark in the build directory though before compiling the plugin on it's own in this manner. You'll find in practice there's only a little time difference between the "full" build and just building the plugin.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '16, 15:51</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-51164" class="comments-container"><span id="51167"></span><div id="comment-51167" class="comment"><div id="post-51167-score" class="comment-score"></div><div class="comment-text"><p>Thank you Grahamb, I have got it working now.</p></div><div id="comment-51167-info" class="comment-info"><span class="comment-age">(24 Mar '16, 19:40)</span> rbw006</div></div><span id="51171"></span><div id="comment-51171" class="comment"><div id="post-51171-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-51171-info" class="comment-info"><span class="comment-age">(25 Mar '16, 01:01)</span> Jaap ♦</div></div></div><div id="comment-tools-51164" class="comment-tools"></div><div class="clear"></div><div id="comment-51164-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

