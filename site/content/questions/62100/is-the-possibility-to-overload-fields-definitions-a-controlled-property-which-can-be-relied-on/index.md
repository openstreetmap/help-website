+++
type = "question"
title = "Is the possibility to overload fields&#x27; definitions a controlled property which can be relied on?"
description = '''Probably one for the core development team. The Lua API reference manual doesn&#x27;t mention this, but if you define a ProtoField whose abbr matches an already existing one contributed by another dissector, it is accepted unless its definition differs from that of the existing one. It is even possible t...'''
date = "2017-06-18T08:34:00Z"
lastmod = "2017-06-26T06:38:00Z"
weight = 62100
keywords = [ "lua", "protofield" ]
aliases = [ "/questions/62100" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is the possibility to overload fields' definitions a controlled property which can be relied on?](/questions/62100/is-the-possibility-to-overload-fields-definitions-a-controlled-property-which-can-be-relied-on)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62100-score" class="post-score" title="current number of votes">0</div><span id="post-62100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Probably one for the core development team.</p><p>The <a href="https://www.wireshark.org/docs/wsdg_html_chunked/wsluarm_modules.html">Lua API reference manual</a> doesn't mention this, but if you define a <code>ProtoField</code> whose <code>abbr</code> matches an already existing one contributed by another dissector, it is accepted unless its definition differs from that of the existing one.</p><p>It is even possible to refer to your own translation table in the <code>ProtoField</code> definition, and such table may be a local one so it clearly doesn't interfere with the other dissector's one.</p><p>As this turned out to be quite useful, my question is whether it is a controlled property and thus it is going to stay like that and should be explicitly documented, or whether it has just "happened" and thus it cannot be relied upon for the future.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-protofield" rel="tag" title="see questions tagged &#39;protofield&#39;">protofield</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jun '17, 08:34</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-62100" class="comments-container"></div><div id="comment-tools-62100" class="comment-tools"></div><div class="clear"></div><div id="comment-62100-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62123"></span>

<div id="answer-container-62123" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62123-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62123-score" class="post-score" title="current number of votes">0</div><span id="post-62123-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sindy has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, this is a feature and will thus likely stick around. From README.dissector:</p><pre><code>It is OK to have header fields with a different format be registered with
the same abbreviation. For instance, the following is valid:

static hf_register_info hf[] = {

    { &amp;hf_field_8bit, /* 8-bit version of proto.field */
    { &quot;Field (8 bit)&quot;, &quot;proto.field&quot;, FT_UINT8, BASE_DEC, NULL,
        0x00, &quot;Field represents FOO&quot;, HFILL }},

    { &amp;hf_field_32bit, /* 32-bit version of proto.field */
    { &quot;Field (32 bit)&quot;, &quot;proto.field&quot;, FT_UINT32, BASE_DEC, NULL,
        0x00, &quot;Field represents FOO&quot;, HFILL }}
};</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '17, 07:41</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-62123" class="comments-container"><span id="62124"></span><div id="comment-62124" class="comment"><div id="post-62124-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot. Does it make sense to advertise this feature at the Lua API wiki?</p></div><div id="comment-62124-info" class="comment-info"><span class="comment-age">(19 Jun '17, 08:00)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="62130"></span><div id="comment-62130" class="comment"><div id="post-62130-score" class="comment-score"></div><div class="comment-text"><p>I don't see why not.</p></div><div id="comment-62130-info" class="comment-info"><span class="comment-age">(19 Jun '17, 11:36)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="62188"></span><div id="comment-62188" class="comment"><div id="post-62188-score" class="comment-score"></div><div class="comment-text"><p>I do :-) First, I cannot decide which would be the right place for this information in the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/wsluarm_modules.html">Lua API reference manual</a>, and second(ary), it is not a Wiki so I can only send the text to the core developers once I find the right place and, subsequently, wording.</p></div><div id="comment-62188-info" class="comment-info"><span class="comment-age">(20 Jun '17, 12:07)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="62301"></span><div id="comment-62301" class="comment"><div id="post-62301-score" class="comment-score"></div><div class="comment-text"><p>Actually the reference manual is stored in git so a <a href="https://wiki.wireshark.org/Development/SubmittingPatches">patch</a> would be the best way to change that (not an email).</p><p>Given that I have probably never used the Lua documentation I couldn't suggest a place for it...</p></div><div id="comment-62301-info" class="comment-info"><span class="comment-age">(26 Jun '17, 06:38)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-62123" class="comment-tools"></div><div class="clear"></div><div id="comment-62123-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

