+++
type = "question"
title = "Converting bytes to table for Lua dissector doesn&#x27;t work"
description = '''See this question: Converting bytes to table in Lua doesn&#x27;t work in 5.2.4 for some background information. I&#x27;m writing a Lua dissector that tries to decrypt AES packets, and I&#x27;m using aeslua to achieve this, but there&#x27;s one line within that code that Lua doesn&#x27;t like: local pwBytes = { string.byte(p...'''
date = "2017-02-11T17:47:00Z"
lastmod = "2017-02-11T17:47:00Z"
weight = 59347
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/59347" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Converting bytes to table for Lua dissector doesn't work](/questions/59347/converting-bytes-to-table-for-lua-dissector-doesnt-work)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59347-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59347-score" class="post-score" title="current number of votes">0</div><span id="post-59347-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>See this question: <a href="http://stackoverflow.com/questions/42182863/converting-bytes-to-table-in-lua-doesnt-work-in-5-2-4">Converting bytes to table in Lua doesn't work in 5.2.4</a> for some background information.</p><p>I'm writing a Lua dissector that tries to decrypt AES packets, and I'm using <a href="https://github.com/SquidDev-CC/aeslua">aeslua</a> to achieve this, but there's one line within that code that Lua doesn't like:</p><pre><code>local pwBytes = { string.byte(password,1,#password)}</code></pre><p>That line <a href="https://tio.run/nexus/lua#@5@Tn5yYo1CQWFxcnl@UomCroOTo5Ozi6gYllbigCsqdKktSi4Hy1cUlRZl56XpJQL4GTJ@OoY4yjK1Zy1UAVFGiAdWjyZWWX6SQrVOmkJmnkFmQmFlUDJdSSMnnUlCAKAeq0ORKzUv5/x8A">runs fine</a> when I Try It Online, and someone over on SO <a href="http://stackoverflow.com/a/42183065/2301484">reported</a> that it works fine in stock 5.2.4, so I'm not sure what's going on.</p><p>This is happening on Linux (Ubuntu 14.04, Wireshark v1.10.6, installed via apt-get) and on Windows (Windows 10, Wireshark v2.2.4, installed via pre-built binary)</p><p>So how can I fix this issue? For now it's not a problem, because I'm using luagcrypt, but switching to pure Lua would be much easier for cross-platform dissecting.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '17, 17:47</strong></p><img src="https://secure.gravatar.com/avatar/990de5d4281890f3136f7b4a5e56b2dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Grayda&#39;s gravatar image" /><p><span>Grayda</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Grayda has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Feb '17, 01:52</strong> </span></p></div></div><div id="comments-container-59347" class="comments-container"></div><div id="comment-tools-59347" class="comment-tools"></div><div class="clear"></div><div id="comment-59347-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

