+++
type = "question"
title = "TAP values in I/O Graph"
description = '''Hi,  I&#x27;ve got a dissector in LUA for my own protocol and a TAP to calculate other values : for example number of packets send :  function tap.packet(pinfo, buffer) counter = counter + 1  end  function tap.draw(t) window:append(&quot;number of packets : &quot; .. counter .. &quot;&#92;n&quot;) end  Is it possible to plot th...'''
date = "2017-02-09T07:30:00Z"
lastmod = "2017-02-09T07:30:00Z"
weight = 59287
keywords = [ "dissector", "tap", "iograph" ]
aliases = [ "/questions/59287" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TAP values in I/O Graph](/questions/59287/tap-values-in-io-graph)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59287-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59287-score" class="post-score" title="current number of votes">0</div><span id="post-59287-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I've got a dissector in LUA for my own protocol and a TAP to calculate other values : for example number of packets send :</p><pre><code>function tap.packet(pinfo, buffer)
counter = counter + 1 
end

function tap.draw(t)
window:append(&quot;number of packets : &quot; .. counter .. &quot;\n&quot;)
end</code></pre><p>Is it possible to plot the <code>counter</code> value in the wireshark I/O Graph tool ? I guess I need to put <code>counter</code> in a field but I don't find how to do that.</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-tap" rel="tag" title="see questions tagged &#39;tap&#39;">tap</span> <span class="post-tag tag-link-iograph" rel="tag" title="see questions tagged &#39;iograph&#39;">iograph</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '17, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/48a6873092325b8870fe6cf20263e051?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Schafer&#39;s gravatar image" /><p><span>Schafer</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Schafer has no accepted answers">0%</span></p></div></div><div id="comments-container-59287" class="comments-container"></div><div id="comment-tools-59287" class="comment-tools"></div><div class="clear"></div><div id="comment-59287-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

