+++
type = "question"
title = "Input for a dissector"
description = '''Hi, I&#x27;m writing a dissector for Wireshark with lua. (not the first). But I have the following problem. Analyzing the data that I want to be split among the TCP level is already to some extent by an ISO 8075.(COPT Protocol) And I just want to be among the Datadump. Use for my dissector. Currently I u...'''
date = "2011-04-07T23:32:00Z"
lastmod = "2011-04-28T14:05:00Z"
weight = 3398
keywords = [ "lua", "dissector", "cotp" ]
aliases = [ "/questions/3398" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Input for a dissector](/questions/3398/input-for-a-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3398-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3398-score" class="post-score" title="current number of votes">1</div><span id="post-3398-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm writing a dissector for Wireshark with lua. (not the first).</p><p>But I have the following problem. Analyzing the data that I want to be split among the TCP level is already to some extent by an ISO 8075.(COPT Protocol) And I just want to be among the Datadump. Use for my dissector.</p><p>Currently I use: tcp_encap_table DissectorTable.get = ("tcp.port) tcp_encap_table: add (102, matze_proto) Here I get data data I do not want to use.</p><p>Is there any way the possibility of something similar as tcp_encap_table DissectorTable.get = ("ISO-8073") tcp_encap_table: add (***, matze_proto) to get to run? I think I need the name of the dissectortable copt(ISO-8073). But I don´t know where i can find it.</p><p>Im greatly appreciate for any help or suggestions.</p><p>Greeting Matze</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-cotp" rel="tag" title="see questions tagged &#39;cotp&#39;">cotp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Apr '11, 23:32</strong></p><img src="https://secure.gravatar.com/avatar/1e76c62e4c9e0e265f3d49ad1ea8f2e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MatzeB&#39;s gravatar image" /><p><span>MatzeB</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MatzeB has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> retagged <strong>29 Apr '11, 22:03</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-3398" class="comments-container"><span id="3399"></span><div id="comment-3399" class="comment"><div id="post-3399-score" class="comment-score"></div><div class="comment-text"><p>Sorry for my bad english:-)</p></div><div id="comment-3399-info" class="comment-info"><span class="comment-age">(07 Apr '11, 23:33)</span> <span class="comment-user userinfo">MatzeB</span></div></div></div><div id="comment-tools-3398" class="comment-tools"></div><div class="clear"></div><div id="comment-3398-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3795"></span>

<div id="answer-container-3795" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3795-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3795-score" class="post-score" title="current number of votes">1</div><span id="post-3795-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>ISO 8073 is actually <strong><a href="http://wiki.wireshark.org/COTP">COTP</a></strong> (Connection Oriented Transport Protocol), not "COPT". here is an example of using <a href="http://wiki.wireshark.org/Lua/Dissectors">dissector chaining</a> to get to the COTP data:</p><pre><code>do
        local cotp_wrapper_proto = Proto(&quot;cotp_wrapper&quot;, &quot;COTP Wrapper&quot;);
        local original_cotp_dissector = nil

        -- Declare a field extractor to check for the
        -- presence of COTP in the current packet.
        local f_cotp = Field.new(&quot;cotp&quot;)

        function cotp_wrapper_proto.dissector(tvbuffer, pinfo, treeitem)

                -- let the actual dissector parse the data at TCP port 102
                -- (it might not be COTP but we&#39;ll find out soon below)
                if original_cotp_dissector then
                    original_cotp_dissector:call(tvbuffer, pinfo, treeitem)
                end

                -- if the &quot;cotp&quot; field exists, the packet has COTP and
                -- tvbuffer is the COTP data
                if f_cotp() then
                    debug(&quot;COTP: &quot; .. tostring(tvbuffer))
                end
        end

        local tcp_dissector_table = DissectorTable.get(&quot;tcp.port&quot;)
        original_cotp_dissector = tcp_dissector_table:get_dissector(102) -- save the original dissector so we can still get to it
        tcp_dissector_table:add(102, cotp_wrapper_proto)                 -- and take its place in the dissector table
end</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '11, 14:05</strong></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p><span>bstn</span><br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bstn has 4 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Apr '11, 14:06</strong> </span></p></div></div><div id="comments-container-3795" class="comments-container"></div><div id="comment-tools-3795" class="comment-tools"></div><div class="clear"></div><div id="comment-3795-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

