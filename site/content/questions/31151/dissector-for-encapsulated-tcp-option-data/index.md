+++
type = "question"
title = "dissector for encapsulated tcp option data"
description = '''Hi, I&#x27;m writing a post-dissector, to process some bespoke TCP options. Im having problems processing the TCP options where the TCP packet is encapsulated. Since TVB is the full buffer, I just want the offset of the TCP.OPTIONS ? and process that! or even better, how can i just take the tcp.options u...'''
date = "2014-03-25T07:33:00Z"
lastmod = "2014-04-04T15:16:00Z"
weight = 31151
keywords = [ "encapsulation", "tcp", "lua" ]
aliases = [ "/questions/31151" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [dissector for encapsulated tcp option data](/questions/31151/dissector-for-encapsulated-tcp-option-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31151-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31151-score" class="post-score" title="current number of votes">0</div><span id="post-31151-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm writing a post-dissector, to process some bespoke TCP options.</p><p>Im having problems processing the TCP options where the TCP packet is encapsulated. Since TVB is the full buffer, I just want the offset of the TCP.OPTIONS ?</p><p>and process that!</p><p>or even better, how can i just take the tcp.options userdata, and process that? - I have to iterate over the tcp option data, as there can be many OPTIONS</p><p>thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-encapsulation" rel="tag" title="see questions tagged &#39;encapsulation&#39;">encapsulation</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '14, 07:33</strong></p><img src="https://secure.gravatar.com/avatar/1a4afaac72ee3ba3540eecb3484b5fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesM&#39;s gravatar image" /><p><span>JamesM</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesM has no accepted answers">0%</span></p></div></div><div id="comments-container-31151" class="comments-container"></div><div id="comment-tools-31151" class="comment-tools"></div><div class="clear"></div><div id="comment-31151-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31157"></span>

<div id="answer-container-31157" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31157-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31157-score" class="post-score" title="current number of votes">1</div><span id="post-31157-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>How about using the "tcp.options" Field to get just the ByteArray of the TCP options?</p><p>Like so:</p><pre><code>local myproto = Proto(&quot;MyTcpOpts&quot;,&quot;Fake proto example to get at TCP options&quot;)

local tcp_opts = Field.new(&quot;tcp.options&quot;)

function myproto.dissector(tvb,pinfo,tree)
    local tcp_opt_finfo = tcp_opts()
    if tcp_opt_finfo then
        local bytearray = tcp_opt_finfo()
        print(&quot;opts bytes length =&quot; .. bytearray:len())
        print(&quot;opts bytes in hex =&quot; .. tostring(bytearray))

        -- do stuff to tcp options here

    else
        print(&quot;no tcp options&quot;)
    end
end

register_postdissector(myproto)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '14, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-31157" class="comments-container"><span id="31535"></span><div id="comment-31535" class="comment"><div id="post-31535-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the response :)</p><p>I did try this, but had "newbie" issues manipulating the ByteArray.</p><p>Will give it another go!</p></div><div id="comment-31535-info" class="comment-info"><span class="comment-age">(04 Apr '14, 15:16)</span> <span class="comment-user userinfo">JamesM</span></div></div></div><div id="comment-tools-31157" class="comment-tools"></div><div class="clear"></div><div id="comment-31157-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

