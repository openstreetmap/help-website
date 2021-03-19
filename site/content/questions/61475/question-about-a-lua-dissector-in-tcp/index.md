+++
type = "question"
title = "Question about a lua dissector in TCP"
description = '''Here is the thing.  source port is an ephemeral port and destination port is 5001 (iperf)  I&#x27;m trying to create a dissector which dissects the ACK packets from destination to source port.  Code 1.  local tcp_dissector_table = DissectorTable.get(&quot;tcp.port&quot;)  tcp_dissector_table:add(5001, my_proto)  w...'''
date = "2017-05-17T22:41:00Z"
lastmod = "2017-05-17T22:41:00Z"
weight = 61475
keywords = [ "lua", "dissector", "postdissector" ]
aliases = [ "/questions/61475" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Question about a lua dissector in TCP](/questions/61475/question-about-a-lua-dissector-in-tcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61475-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61475-score" class="post-score" title="current number of votes">0</div><span id="post-61475-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Here is the thing.</p><ul><li>source port is an ephemeral port and destination port is 5001 (iperf)</li><li>I'm trying to create a dissector which dissects the ACK packets from destination to source port.</li></ul><p>Code 1.</p><pre><code>      local tcp_dissector_table = DissectorTable.get(&quot;tcp.port&quot;)
      tcp_dissector_table:add(5001, my_proto)</code></pre><p>with the code 1., it dissects only the packets from source to destination.</p><p>So I solved the problem with the code 2.</p><p>Code 2.</p><pre><code>    function my_proto.dissector(buffer, pinfo, root)
      if f_tcp_srcport().value == 5001 then
      --my source
      end
    end

    register_postdissector(my_proto)</code></pre><p>The question is 'why does the code 3. not work as it did like Code 1.?".</p><p>Code 3.</p><pre><code>local tcp_dissector_table = DissectorTable.get(&quot;tcp.port&quot;)
tcp_dissector_table:add(5001, my_proto)</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-postdissector" rel="tag" title="see questions tagged &#39;postdissector&#39;">postdissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '17, 22:41</strong></p><img src="https://secure.gravatar.com/avatar/3a702eaa9f4d90c81f74480545063c71?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ngn505&#39;s gravatar image" /><p><span>ngn505</span><br />
<span class="score" title="6 reputation points">6</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ngn505 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 May '17, 00:48</strong> </span></p></div></div><div id="comments-container-61475" class="comments-container"></div><div id="comment-tools-61475" class="comment-tools"></div><div class="clear"></div><div id="comment-61475-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

