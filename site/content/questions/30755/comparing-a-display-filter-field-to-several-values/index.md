+++
type = "question"
title = "Comparing a &quot;display filter&quot; field to several values"
description = '''I&#x27;m using the following code in display filter: wlan_mgt.supported_rates==0x12 &amp;amp;&amp;amp; wlan_mgt.supported_rates==0x24 &amp;amp;&amp;amp; wlan_mgt.supported_rates==0x48 &amp;amp;&amp;amp; wlan_mgt.supported_rates==0x6c &amp;amp;&amp;amp; wlan_mgt.supported_rates==0x82 &amp;amp;&amp;amp; wlan_mgt.supported_rates==0x84 &amp;amp;&amp;amp; ...'''
date = "2014-03-13T03:00:00Z"
lastmod = "2014-03-19T08:55:00Z"
weight = 30755
keywords = [ "display-filter" ]
aliases = [ "/questions/30755" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Comparing a "display filter" field to several values](/questions/30755/comparing-a-display-filter-field-to-several-values)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30755-score" class="post-score" title="current number of votes">0</div><span id="post-30755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using the following code in display filter:</p><pre><code>wlan_mgt.supported_rates==0x12 &amp;&amp;
wlan_mgt.supported_rates==0x24 &amp;&amp;
wlan_mgt.supported_rates==0x48 &amp;&amp;
wlan_mgt.supported_rates==0x6c &amp;&amp;
wlan_mgt.supported_rates==0x82 &amp;&amp;
wlan_mgt.supported_rates==0x84 &amp;&amp;
wlan_mgt.supported_rates==0x8b &amp;&amp;
wlan_mgt.supported_rates==0x96</code></pre><p>Is it possible to minimize it to something like this (doesn't work):</p><pre><code>wlan_mgt.supported_rates==(0x12 &amp;&amp; 0x24 &amp;&amp; 0x48 &amp;&amp; 0x6c &amp;&amp; 0x82 &amp;&amp; 0x84 &amp;&amp; 0x8b &amp;&amp; 0x96)</code></pre><p>?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '14, 03:00</strong></p><img src="https://secure.gravatar.com/avatar/d7bc992d0b3f0e2db1bf0eec41ba32dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dor_lan&#39;s gravatar image" /><p><span>Dor_lan</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dor_lan has no accepted answers">0%</span></p></div></div><div id="comments-container-30755" class="comments-container"></div><div id="comment-tools-30755" class="comment-tools"></div><div class="clear"></div><div id="comment-30755-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="30759"></span>

<div id="answer-container-30759" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30759-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30759-score" class="post-score" title="current number of votes">1</div><span id="post-30759-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>frame contains 12:24:48:6c:82:84:8b:96</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '14, 05:28</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p><span>Roland</span><br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-30759" class="comments-container"><span id="30760"></span><div id="comment-30760" class="comment"><div id="post-30760-score" class="comment-score"></div><div class="comment-text"><p>I don't think that's correct, the byte sequence for "contains" is in sequential order, whereas the OP requires any of the values in a single field.</p><p>I don't think it can be done.</p></div><div id="comment-30760-info" class="comment-info"><span class="comment-age">(13 Mar '14, 05:33)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="30761"></span><div id="comment-30761" class="comment"><div id="post-30761-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span>: not "any of the values", but the packet has to contain this field multiple times, whereas each time it equals to <em>another</em> value in the list.</p></div><div id="comment-30761-info" class="comment-info"><span class="comment-age">(13 Mar '14, 05:39)</span> <span class="comment-user userinfo">Dor_lan</span></div></div><span id="30762"></span><div id="comment-30762" class="comment"><div id="post-30762-score" class="comment-score"></div><div class="comment-text"><p>OK misunderstood the question, the filter supplied by <span>@Roland</span> will work if the field is a single byte, the repeated fields follow one another with no intervening space and the repeated fields always have the value in the order specified.</p><p><span>@Dor_lan</span> Have you tried the filter?</p></div><div id="comment-30762-info" class="comment-info"><span class="comment-age">(13 Mar '14, 05:56)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="30949"></span><div id="comment-30949" class="comment"><div id="post-30949-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span>: Yes, I've tried the display filter <code>frame.number==1 &amp;&amp; wlan_mgt.supported_rates contains 12:24:48:6c:82:84:8b:96</code> and tshark returned the error <em>"tshark: wlan_mgt.supported_rates (type=unsigned, 1 byte) cannot participate in 'contains' comparison."</em>.</p></div><div id="comment-30949-info" class="comment-info"><span class="comment-age">(19 Mar '14, 06:37)</span> <span class="comment-user userinfo">Dor_lan</span></div></div><span id="30951"></span><div id="comment-30951" class="comment"><div id="post-30951-score" class="comment-score"></div><div class="comment-text"><p>You're only able to run contains against the whole frame not that field, as each instance of the field can only contain 1 byte.</p><p>What happens with the filter as suggested by <span>@Roland</span>?</p></div><div id="comment-30951-info" class="comment-info"><span class="comment-age">(19 Mar '14, 06:50)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="30954"></span><div id="comment-30954" class="comment not_top_scorer"><div id="post-30954-score" class="comment-score"></div><div class="comment-text"><p>I am offended by the down vote. You just have to copy and paste the command, no need to change it. grahamb explained how the command works. If you want to narrow it down you can use 'frame[offset] contains byte:byte:byte' or just right click on Tag: Supported Rates and prepare filter for selected. I also agree that a display filter button or macro is the way to go if you need to filter for the above all the time.</p></div><div id="comment-30954-info" class="comment-info"><span class="comment-age">(19 Mar '14, 08:38)</span> <span class="comment-user userinfo">Roland</span></div></div><span id="30956"></span><div id="comment-30956" class="comment not_top_scorer"><div id="post-30956-score" class="comment-score"></div><div class="comment-text"><p><span>@Roland</span>: Sorry for the votedown, I misunderstood the usage with <code>contains</code>. I've tried <code>frame.number==1 &amp;&amp; frame contains 12:24:48:6c:82:84:8b:96</code> and also <code>frame.number==1 &amp;&amp; wlan_mgt contains 12:24:48:6c:82:84:8b:96</code> and both worked! Thank you :)</p></div><div id="comment-30956-info" class="comment-info"><span class="comment-age">(19 Mar '14, 08:55)</span> <span class="comment-user userinfo">Dor_lan</span></div></div></div><div id="comment-tools-30759" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-30759-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30776"></span>

<div id="answer-container-30776" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30776-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30776-score" class="post-score" title="current number of votes">1</div><span id="post-30776-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think it's going to give you <em>exactly</em> what you want, but maybe a <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChDisplayFilterMacrosSection.html">Display Filter Macro</a> will help, by at least reducing the amount of typing you need to do?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '14, 11:17</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-30776" class="comments-container"><span id="30950"></span><div id="comment-30950" class="comment"><div id="post-30950-score" class="comment-score"></div><div class="comment-text"><p>Though not a direct solution but does help! :)</p></div><div id="comment-30950-info" class="comment-info"><span class="comment-age">(19 Mar '14, 06:38)</span> <span class="comment-user userinfo">Dor_lan</span></div></div></div><div id="comment-tools-30776" class="comment-tools"></div><div class="clear"></div><div id="comment-30776-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

