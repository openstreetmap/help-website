+++
type = "question"
title = "in ue aggregatemaximum bitrate ie of ranap  not able to display the values"
description = '''in ue aggregatemaximum bitrate ie of ranap iam able to display the present bit map of ue aggregate-maximum bit rate down link and ue aggregate-maximum bit-rate down-link also the constrained integer length for the both on wire-shark .but iam not able to display both the vales on wire-shark . iam get...'''
date = "2012-09-24T05:53:00Z"
lastmod = "2012-09-26T00:34:00Z"
weight = 14478
keywords = [ "max", "bitrate" ]
aliases = [ "/questions/14478" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [in ue aggregatemaximum bitrate ie of ranap not able to display the values](/questions/14478/in-ue-aggregatemaximum-bitrate-ie-of-ranap-not-able-to-display-the-values)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14478-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14478-score" class="post-score" title="current number of votes">0</div><span id="post-14478-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>in ue aggregatemaximum bitrate ie of ranap iam able to display the present bit map of ue aggregate-maximum bit rate down link and ue aggregate-maximum bit-rate down-link also the constrained integer length for the both on wire-shark .but iam not able to display both the vales on wire-shark . iam getting dissector bug , protocol RANAP: proto.c 3043 failed assertion "hfinfo-&gt;type == FT_UINT64</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-max" rel="tag" title="see questions tagged &#39;max&#39;">max</span> <span class="post-tag tag-link-bitrate" rel="tag" title="see questions tagged &#39;bitrate&#39;">bitrate</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '12, 05:53</strong></p><img src="https://secure.gravatar.com/avatar/0ffa9d5df2804dc37ef6011fb54f1ed5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vijeth&#39;s gravatar image" /><p><span>vijeth</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vijeth has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Sep '12, 06:01</strong> </span></p></div></div><div id="comments-container-14478" class="comments-container"><span id="14479"></span><div id="comment-14479" class="comment"><div id="post-14479-score" class="comment-score"></div><div class="comment-text"><p>Could you raise a bug attaching a small sample file showing the bug? Is this a unmodified wireshark or have you modified the RANAP dissector? The spec says UE-AggregateMaximumBitRateDownlink ::= INTEGER (1..1000000000) which should fit in an UINT32</p></div><div id="comment-14479-info" class="comment-info"><span class="comment-age">(24 Sep '12, 07:33)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="14495"></span><div id="comment-14495" class="comment"><div id="post-14495-score" class="comment-score"></div><div class="comment-text"><p><img src="https://osqa-ask.wireshark.org/upfiles/bug.jpeg" alt="alt text" /></p></div><div id="comment-14495-info" class="comment-info"><span class="comment-age">(24 Sep '12, 23:13)</span> <span class="comment-user userinfo">vijeth</span></div></div><span id="14496"></span><div id="comment-14496" class="comment"><div id="post-14496-score" class="comment-score"></div><div class="comment-text"><p>Can you try a more recent version e.g. 1.8.2 as your version (1.5.1) is quite old and is also a development version.</p></div><div id="comment-14496-info" class="comment-info"><span class="comment-age">(24 Sep '12, 23:33)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="14532"></span><div id="comment-14532" class="comment"><div id="post-14532-score" class="comment-score"></div><div class="comment-text"><p>no it doesn't work for 1.8.2 . any other solution for this simple problem ??</p></div><div id="comment-14532-info" class="comment-info"><span class="comment-age">(25 Sep '12, 23:36)</span> <span class="comment-user userinfo">vijeth</span></div></div><span id="14533"></span><div id="comment-14533" class="comment"><div id="post-14533-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately not, you'll just have to follow Anders' advice and raise a bug on the <a href="https://bugs.wireshark.org/bugzilla/">Wireshark bugzilla</a> and attach a small capture showing the problem.</p></div><div id="comment-14533-info" class="comment-info"><span class="comment-age">(26 Sep '12, 00:34)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-14478" class="comment-tools"></div><div class="clear"></div><div id="comment-14478-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

