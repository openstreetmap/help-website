+++
type = "question"
title = "My Lua dissector isn&#x27;t finding the CRC32 module"
description = '''Hi, I have a .lua file. Can I get please instructions how to add it the wireshark and decode my message correctly (I have wireshark with version 1.8.6)? I added it to my personal plugins folder and this is the message code every time I launch the program. Lua: Error during loading:  [string &quot;C:&#92;User...'''
date = "2013-08-07T14:43:00Z"
lastmod = "2013-08-09T05:09:00Z"
weight = 23622
keywords = [ "lua", "require" ]
aliases = [ "/questions/23622" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [My Lua dissector isn't finding the CRC32 module](/questions/23622/my-lua-dissector-isnt-finding-the-crc32-module)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23622-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23622-score" class="post-score" title="current number of votes">0</div><span id="post-23622-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a .lua file. Can I get please instructions how to add it the wireshark and decode my message correctly (I have wireshark with version 1.8.6)?</p><p>I added it to my personal plugins folder and this is the message code every time I launch the program.</p><pre><code>Lua: Error during loading:
 [string &quot;C:\Users\morton.sherwood\AppData\Roaming\Wi...&quot;]:7: module &#39;CRC32&#39; not found:
    no field package.preload[&#39;CRC32&#39;]
    no file &#39;.\CRC32.lua&#39;
    no file &#39;C:\Program Files (x86)\Wireshark\lua\CRC32.lua&#39;
    no file &#39;C:\Program Files (x86)\Wireshark\lua\CRC32\init.lua&#39;
    no file &#39;C:\Program Files (x86)\Wireshark\CRC32.lua&#39;
    no file &#39;C:\Program Files (x86)\Wireshark\CRC32\init.lua&#39;
    no file &#39;.\CRC32.dll&#39;
    no file &#39;.\CRC3251.dll&#39;
    no file &#39;C:\Program Files (x86)\Wireshark\CRC32.dll&#39;
    no file &#39;C:\Program Files (x86)\Wireshark\CRC3251.dll&#39;
    no file &#39;C:\Program Files (x86)\Wireshark\clibs\CRC32.dll&#39;
    no file &#39;C:\Program Files (x86)\Wireshark\clibs\CRC3251.dll&#39;
    no file &#39;C:\Program Files (x86)\Wireshark\loadall.dll&#39;
    no file &#39;C:\Program Files (x86)\Wireshark\clibs\loadall.dll&#39;</code></pre><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-require" rel="tag" title="see questions tagged &#39;require&#39;">require</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Aug '13, 14:43</strong></p><img src="https://secure.gravatar.com/avatar/182ef93b70cfdfc6b73831b8970f01b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="morton&#39;s gravatar image" /><p><span>morton</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="morton has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Aug '13, 00:27</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-23622" class="comments-container"><span id="23623"></span><div id="comment-23623" class="comment"><div id="post-23623-score" class="comment-score"></div><div class="comment-text"><p>Could you please show some or all of the Lua code for your dissector? Make sure what code is included is the code that's trying to use "CRC32".</p></div><div id="comment-23623-info" class="comment-info"><span class="comment-age">(07 Aug '13, 18:58)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="23626"></span><div id="comment-23626" class="comment"><div id="post-23626-score" class="comment-score"></div><div class="comment-text"><p>Hi, I cannot show all the code, but I have this line:</p><p>require('CRC32')</p><p>this is the only line I have in my code which refernce to CRC32.</p><p>Thank you</p></div><div id="comment-23626-info" class="comment-info"><span class="comment-age">(07 Aug '13, 23:30)</span> <span class="comment-user userinfo">morton</span></div></div></div><div id="comment-tools-23622" class="comment-tools"></div><div class="clear"></div><div id="comment-23622-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23627"></span>

<div id="answer-container-23627" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23627-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23627-score" class="post-score" title="current number of votes">1</div><span id="post-23627-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cmaynard has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p><code>require('CRC32')</code></p></blockquote><p>As <a href="http://www.lua.org/manual/5.1/manual.html#pdf-require">the documentation for <code>require</code> says</a>, it loads the module with the name passed to it as an argument. This means that you will need to have a <code>CRC32</code> module available; either you <em>don't</em> have it available, in which case you will have to add it to your Lua installation, or it's not in one of the directories in which it's searching, in which case you will somehow have to configure Lua to search for it where it's loaded.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '13, 00:26</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23627" class="comments-container"><span id="23672"></span><div id="comment-23672" class="comment"><div id="post-23672-score" class="comment-score"></div><div class="comment-text"><p>Thank you It solves my problem</p></div><div id="comment-23672-info" class="comment-info"><span class="comment-age">(09 Aug '13, 02:50)</span> <span class="comment-user userinfo">morton</span></div></div><span id="23675"></span><div id="comment-23675" class="comment"><div id="post-23675-score" class="comment-score"></div><div class="comment-text"><p>If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-23675-info" class="comment-info"><span class="comment-age">(09 Aug '13, 05:09)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-23627" class="comment-tools"></div><div class="clear"></div><div id="comment-23627-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

