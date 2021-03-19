+++
type = "question"
title = "LUA scripting - Matching multiple instances of multiples fields"
description = '''There is two fields(rtcp.ssrc.fraction and rtcp.ssrc.cum_nr) that can have multiple instances on a single packet. I want to traverse all instances of rtcp.ssrc.fraction and then find the &quot;matching instance&quot; of rtcp.ssrc.cum_nr. See example below.  A packet has three RTCP messages: EXTENDED REPORT (E...'''
date = "2016-04-18T00:11:00Z"
lastmod = "2016-04-18T00:11:00Z"
weight = 51742
keywords = [ "lua", "rtcp", "multiple", "instances" ]
aliases = [ "/questions/51742" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [LUA scripting - Matching multiple instances of multiples fields](/questions/51742/lua-scripting-matching-multiple-instances-of-multiples-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51742-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51742-score" class="post-score" title="current number of votes">0</div><span id="post-51742-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>There is two fields(rtcp.ssrc.fraction and rtcp.ssrc.cum_nr) that can have multiple instances on a single packet. I want to traverse all instances of rtcp.ssrc.fraction and then find the "matching instance" of rtcp.ssrc.cum_nr. See example below.</p><p>A packet has three RTCP messages: EXTENDED REPORT (ER), SENDER REPORT (SR), SOURCE DESCRIPTION (SD)</p><p>Both ER and SR include instances of rtcp.ssrc.fration but only SR includes an instance of rtcp.ssrc.cum_nr.</p><pre><code>local fractions = { rtcp_fraction() }                                
local cumulatives = { rtcp_cumulative() }

print cumulatives[1].value -- Prints value of cum_nr on SENDER REPORT 
print fractions[1].value -- Prints value of fraction on EXTENDED REPORT
print fractions[2].value -- Prints value of fraction on SENDER REPORT</code></pre><p>How can I know which fraction corresponds to the cumulative value without knowing the order of the RTCP messages on the packet?</p><p>I was hoping the cumulatives table would get filled with nil values for each message that didn't have a cum_nr value, so I could do something like what you see below, but that is not the case, so the code below would work if the SR came before the ER but if the ER comes before the SR it would match the fraction value of the ER to the cumulative of the SR.<br />
</p><pre><code>for k,v in pairs(fractions) do 
  if cumulatives[k] ~= nil then 
    print(&quot;fraction: &quot; .. v .. &quot; cumulative: &quot; .. cumulatives[k].value)
  end
end</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-rtcp" rel="tag" title="see questions tagged &#39;rtcp&#39;">rtcp</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-instances" rel="tag" title="see questions tagged &#39;instances&#39;">instances</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '16, 00:11</strong></p><img src="https://secure.gravatar.com/avatar/af707492ea742ab35070019afc45e174?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jotica&#39;s gravatar image" /><p><span>jotica</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jotica has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Apr '16, 04:06</strong> </span></p></div></div><div id="comments-container-51742" class="comments-container"></div><div id="comment-tools-51742" class="comment-tools"></div><div class="clear"></div><div id="comment-51742-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

