+++
type = "question"
title = "Feature Request: Being able to add a Column which is a calculated field"
description = '''I often need to analyze FIX messages and doing this I could really need a way to be able to create a &quot;calculated field&quot;. e.g. - I have a trace containing FIX stream - I have the OS timestamp when we received the message - I have the FIX time stamp inside the message in SendingTime (Tag52) To be able...'''
date = "2012-09-21T02:31:00Z"
lastmod = "2012-09-24T02:17:00Z"
weight = 14418
keywords = [ "fix", "calculated_field" ]
aliases = [ "/questions/14418" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Feature Request: Being able to add a Column which is a calculated field](/questions/14418/feature-request-being-able-to-add-a-column-which-is-a-calculated-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14418-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14418-score" class="post-score" title="current number of votes">0</div><span id="post-14418-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I often need to analyze FIX messages and doing this I could really need a way to be able to create a "calculated field".</p><p>e.g. - I have a trace containing FIX stream - I have the OS timestamp when we received the message - I have the FIX time stamp inside the message in SendingTime (Tag52)</p><p>To be able to analyze this closer it would be VERY beneficial if it was possible to create a "Calculated Column" and report on that.</p><p>It should be able to specify which original columns to use - e.g. Column name FIXDelay = Tag52-OSTime. This would give a quick picture of the delays caused in the FIX stream. Of cause a way to create a graph for this would also be GREAT!</p><p>Regards Ib Tornøe</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fix" rel="tag" title="see questions tagged &#39;fix&#39;">fix</span> <span class="post-tag tag-link-calculated_field" rel="tag" title="see questions tagged &#39;calculated_field&#39;">calculated_field</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Sep '12, 02:31</strong></p><img src="https://secure.gravatar.com/avatar/41ceec8c367e45ba2a9f88727b6de498?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ITO&#39;s gravatar image" /><p><span>ITO</span><br />
<span class="score" title="-1 reputation points">-1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ITO has no accepted answers">0%</span></p></div></div><div id="comments-container-14418" class="comments-container"><span id="14442"></span><div id="comment-14442" class="comment"><div id="post-14442-score" class="comment-score"></div><div class="comment-text"><p>Interesting idea. I think for now, you would have to use a script to do this offline. You can also checkout commercial analyzers that can decode FIX for you (if you have the right version of FIX as the analyzer). On the right side of this site is the Riverbed/Pilot ad. See if that will be able to help you as it has FIX support.</p></div><div id="comment-14442-info" class="comment-info"><span class="comment-age">(21 Sep '12, 14:11)</span> <span class="comment-user userinfo">hansangb</span></div></div><span id="14445"></span><div id="comment-14445" class="comment"><div id="post-14445-score" class="comment-score"></div><div class="comment-text"><p>Hi hansangb I do have Pilot and that does not have this capability - I have filed a request for new feature. Regarding Wireshark – my idea was to have a common way of adding a column that could contain custom values created out of a formula, where it was possible to do calculations on optional fields in FIX but also in any protocol. Also to be able to use this same formula to draw a graph this would be great. If should send this a new feature request for Wireshark for this feature – where is the right place to do this?</p></div><div id="comment-14445-info" class="comment-info"><span class="comment-age">(21 Sep '12, 23:15)</span> <span class="comment-user userinfo">ITO</span></div></div><span id="14471"></span><div id="comment-14471" class="comment"><div id="post-14471-score" class="comment-score"></div><div class="comment-text"><p>ITO, Scripting is the only way (since FIX views don't support what you need). These types of scripting support is what we (Riverbed) are working on.</p></div><div id="comment-14471-info" class="comment-info"><span class="comment-age">(23 Sep '12, 17:17)</span> <span class="comment-user userinfo">hansangb</span></div></div><span id="14476"></span><div id="comment-14476" class="comment"><div id="post-14476-score" class="comment-score"></div><div class="comment-text"><p>Hi Hansang Bae. I know you are working on this - I have filed the request for this support myself - with this support we can do the same in Pilot as in Corvil. But I would also like to file a request for extension of the functionality natively in Wireshark - where is the preferred place to do that? -Ib Tornøe</p></div><div id="comment-14476-info" class="comment-info"><span class="comment-age">(23 Sep '12, 22:29)</span> <span class="comment-user userinfo">ITO</span></div></div><span id="14477"></span><div id="comment-14477" class="comment"><div id="post-14477-score" class="comment-score"></div><div class="comment-text"><p>The designated place to file feature requests for Wireshark is to file an enhancement request at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a>.</p></div><div id="comment-14477-info" class="comment-info"><span class="comment-age">(24 Sep '12, 02:17)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-14418" class="comment-tools"></div><div class="clear"></div><div id="comment-14418-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14421"></span>

<div id="answer-container-14421" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14421-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14421-score" class="post-score" title="current number of votes">0</div><span id="post-14421-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That's why there is <a href="http://wiki.wireshark.org/Lua">Lua</a> support in Wireshark :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Sep '12, 03:19</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-14421" class="comments-container"><span id="14429"></span><div id="comment-14429" class="comment"><div id="post-14429-score" class="comment-score"></div><div class="comment-text"><p>Thanks ;-)</p></div><div id="comment-14429-info" class="comment-info"><span class="comment-age">(21 Sep '12, 05:19)</span> <span class="comment-user userinfo">ITO</span></div></div></div><div id="comment-tools-14421" class="comment-tools"></div><div class="clear"></div><div id="comment-14421-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

