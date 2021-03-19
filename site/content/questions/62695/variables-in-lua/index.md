+++
type = "question"
title = "variables in lua"
description = '''I&#x27;m using MPTCP(Multipath tcp) I&#x27;m trying just to display duplicated packets by filtering duplicated DSN(data sequence number) There is a filter called &#x27;mptcp.duplicated_dsn&#x27; but never displays the packets though there are duplicated ones.  why does this filter not work? And I&#x27;m trying to make a sim...'''
date = "2017-07-12T02:09:00Z"
lastmod = "2017-07-12T05:52:00Z"
weight = 62695
keywords = [ "variable", "lua", "dissector" ]
aliases = [ "/questions/62695" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [variables in lua](/questions/62695/variables-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62695-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62695-score" class="post-score" title="current number of votes">0</div><span id="post-62695-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using MPTCP(Multipath tcp) I'm trying just to display duplicated packets by filtering duplicated DSN(data sequence number) There is a filter called 'mptcp.duplicated_dsn' but never displays the packets though there are duplicated ones.</p><p>why does this filter not work?</p><p>And I'm trying to make a simple dissector in LUA for this. So I wrote just one DSN of a packet to see if it can dissect by data sequence number. but It never reads the DSN. I think it's because of the length of DSN as I've checked it reads values of other fields which are shorter than DSN. The DSN must be greater than INTEGER number. Probably I need a bigger variable like 'long' in c I can't figure out where to put this bigger variable for the numbers. Can anyone help?</p><pre><code> local r_transmission = Proto(&quot;Rtsm&quot;, &quot;RTSM&quot;)
 local dup_dsn = Field.new.(&quot;tcp.options.mptcp.rawdataseqno&quot;)

  function r_transmission.dissector(buffer, pinfo, root)

    dsn = dup_dsn().value
    if dsn == 1096995081 then
    pinfo.cols.info = &quot;rrrrr&quot;
 end
end

register_postdissector(r_transmission)</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-variable" rel="tag" title="see questions tagged &#39;variable&#39;">variable</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jul '17, 02:09</strong></p><img src="https://secure.gravatar.com/avatar/3a702eaa9f4d90c81f74480545063c71?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ngn505&#39;s gravatar image" /><p><span>ngn505</span><br />
<span class="score" title="6 reputation points">6</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ngn505 has no accepted answers">0%</span></p></div></div><div id="comments-container-62695" class="comments-container"><span id="62698"></span><div id="comment-62698" class="comment"><div id="post-62698-score" class="comment-score"></div><div class="comment-text"><p>The dot between Field.new and ("tcp.options.mptcp.rawdataseqno") is really present in your code or it is only here?</p></div><div id="comment-62698-info" class="comment-info"><span class="comment-age">(12 Jul '17, 05:52)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-62695" class="comment-tools"></div><div class="clear"></div><div id="comment-62695-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

