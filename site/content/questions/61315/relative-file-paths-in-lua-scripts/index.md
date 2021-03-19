+++
type = "question"
title = "Relative file paths in Lua scripts?"
description = '''I have a directory containing my dissector, listener, and subdirectories with libraries. I&#x27;ve been attempting to use dofile, require, and filepath strings to call the libraries along with additional files like so: dofile(&quot;subdirec/script.lua&quot;)  require &quot;subdirec.script&quot;  local filename = &quot;subdirec/f...'''
date = "2017-05-09T15:54:00Z"
lastmod = "2017-05-09T15:54:00Z"
weight = 61315
keywords = [ "relative", "lua", "file", "wireshark" ]
aliases = [ "/questions/61315" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Relative file paths in Lua scripts?](/questions/61315/relative-file-paths-in-lua-scripts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61315-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61315-score" class="post-score" title="current number of votes">0</div><span id="post-61315-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a directory containing my dissector, listener, and subdirectories with libraries. I've been attempting to use dofile, require, and filepath strings to call the libraries along with additional files like so:</p><pre><code>dofile(&quot;subdirec/script.lua&quot;)

require &quot;subdirec.script&quot;

local filename = &quot;subdirec/file.xml&quot;</code></pre><p>However, when I attempt using this syntax and open Wireshark I get the "file does not exist error".</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-relative" rel="tag" title="see questions tagged &#39;relative&#39;">relative</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '17, 15:54</strong></p><img src="https://secure.gravatar.com/avatar/00cd850e8d2944c2c7dcdc13baf50a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Irfan%20Hossain&#39;s gravatar image" /><p><span>Irfan Hossain</span><br />
<span class="score" title="11 reputation points">11</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Irfan Hossain has no accepted answers">0%</span></p></div></div><div id="comments-container-61315" class="comments-container"></div><div id="comment-tools-61315" class="comment-tools"></div><div class="clear"></div><div id="comment-61315-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

