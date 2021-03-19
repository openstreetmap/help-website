+++
type = "question"
title = "Prefs.range handling in lua"
description = '''Hi all, I wonder how to threat Pref.ranges in wiresharks lua interface. I did the following: proto.prefs.ports = Pref.range( &quot;Ports&quot;, &quot;23055-23056&quot;, &quot;Ports&quot;, 65535)  function proto.init()  tcp_port_table = DissectorTable.get(&quot;tcp.port&quot;)  tcp_port_table:add(zeosys_proto.prefs.ports, zeosys_proto)  en...'''
date = "2014-05-15T00:51:00Z"
lastmod = "2014-06-22T13:00:00Z"
weight = 32810
keywords = [ "prefs.range", "lua" ]
aliases = [ "/questions/32810" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Prefs.range handling in lua](/questions/32810/prefsrange-handling-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32810-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32810-score" class="post-score" title="current number of votes">0</div><span id="post-32810-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I wonder how to threat Pref.ranges in wiresharks lua interface. I did the following:</p><pre><code>proto.prefs.ports = Pref.range( &quot;Ports&quot;, &quot;23055-23056&quot;, &quot;Ports&quot;, 65535)

function proto.init()
  tcp_port_table = DissectorTable.get(&quot;tcp.port&quot;)
  tcp_port_table:add(zeosys_proto.prefs.ports, zeosys_proto)  
end</code></pre><p>and got:</p><p>bad argument #1 to 'add' (number expected, got string)</p><p>Should I implement the range parsing on my own or are there built-in functions for this?</p><p>Cheers, Michael</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-prefs.range" rel="tag" title="see questions tagged &#39;prefs.range&#39;">prefs.range</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 May '14, 00:51</strong></p><img src="https://secure.gravatar.com/avatar/518b06859db0266b591d1ca8b4d118c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MichaelAdam&#39;s gravatar image" /><p><span>MichaelAdam</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MichaelAdam has no accepted answers">0%</span></p></div></div><div id="comments-container-32810" class="comments-container"><span id="34045"></span><div id="comment-34045" class="comment"><div id="post-34045-score" class="comment-score"></div><div class="comment-text"><p>What version of Wireshark? Post the contents of the Help | About | Wireshark tab.</p></div><div id="comment-34045-info" class="comment-info"><span class="comment-age">(22 Jun '14, 13:00)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-32810" class="comment-tools"></div><div class="clear"></div><div id="comment-32810-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34044"></span>

<div id="answer-container-34044" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34044-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34044-score" class="post-score" title="current number of votes">0</div><span id="post-34044-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This looks like a bug. The <code>add()</code> function for a <code>DissectorTable</code> of <code>tcp.port</code> should be able to handle a range string argument. Please submit a bug to <a href="https://bugs.wireshark.org/bugzilla/">bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '14, 11:13</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-34044" class="comments-container"></div><div id="comment-tools-34044" class="comment-tools"></div><div class="clear"></div><div id="comment-34044-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

