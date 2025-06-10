+++
type = "question"
title = "iOS/Mac App Store and CC-BY-SA compatibility"
description = '''Is it really allowed to distribute an app containing OSM data on any of iOS/Mac App Store? GPL is incompatible with the App Store, and it seems like CC-BY-SA is similarly incompatible? CC-BY-SA has this requirement:  If you alter, transform, or build upon this work, you may distribute the resulting ...'''
date = "2012-01-08T08:26:00Z"
lastmod = "2012-01-08T16:42:00Z"
weight = 9846
keywords = [ "apple", "license", "cc-by-sa" ]
aliases = [ "/questions/9846" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [iOS/Mac App Store and CC-BY-SA compatibility](/questions/9846/iosmac-app-store-and-cc-by-sa-compatibility)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9846-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9846-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9846-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it really allowed to distribute an app containing OSM data on any of iOS/Mac App Store? GPL is incompatible with the App Store, and it seems like CC-BY-SA is similarly incompatible?</p>
<p>CC-BY-SA has this requirement:</p>
<blockquote>
<p>If you alter, transform, or build upon this work, you may distribute the resulting work only under the same or similar license to this one.</p>
</blockquote>
<p>It seems like this specifically disallows OSM data distributed on the App Store, because Apple requires <em>all</em> apps to be distributed under the standard App Store license:</p>
<blockquote>
<p>You agree that the terms of the Licensed Application End User License Agreement will apply to each Apple Product and to each Third-Party Product that you license through the App Store</p>
</blockquote>
<p>I guess it depends on exactly what the definition of "build upon" means? If the data is unmodified, then it's OK to distribute under the App Store license? It seems like most GPS apps would make at least some customisations to the data.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-apple" rel="tag" title="see questions tagged &#39;apple&#39;">apple</span> <span class="post-tag tag-link-license" rel="tag" title="see questions tagged &#39;license&#39;">license</span> <span class="post-tag tag-link-cc-by-sa" rel="tag" title="see questions tagged &#39;cc-by-sa&#39;">cc-by-sa</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jan '12, 08:26</strong></p>
<img src="https://secure.gravatar.com/avatar/5e9cb9ce6039c30d9efd89ed9199eaab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abhi%20Beckert&#39;s gravatar image" />
<p><span>Abhi Beckert</span><br />
<span class="score" title="71 reputation points">71</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abhi Beckert has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jan '12, 08:27</strong> </span></p>
</div>
</div>
<div id="comments-container-9846" class="comments-container">
&#10;</div>
<div id="comment-tools-9846" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9846-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="9854"></span>

<div id="answer-container-9854" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9854-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9854-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-9854-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Abhi Beckert has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I believe that you are right and that a close legal examination would show that it is a license violation to distribute our content through Apple's platform. As others have pointed out, if you only get the software through the store and the software then downloads the data through an open channel then that's probably fine; if however the data is acquired through Apple's platform then it might not be.</p>
<p>The parapgrah you pointed out is one of the reasons for this; another reason is that recipients of CC-BY-SA data must not only be <em>allowed</em> to share it, there must also not be any technical measures to keep them from exercising that right. I believe that if you buy a product through Apple's platform, you will not be able to share it with other users.</p>
<p>ODbL has a "parallel distribution" clause that would solve the second problem (you can simply offer a share-able version of your product in parallel to the proprietary platform), but the first problem (Apple claiming a certain license) would persist, at least if the product you are distributing is a database. (ODbL has relaxed provisions for non-database products.)</p>
<p>It is very unlikely that CC-BY-SA is compatible with Apple's license because CC-BY-SA explicitly disallows adding any kind of restriction or extra permission to the content, and why would Apple want their own license if not for these reasons?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jan '12, 10:24</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jan '12, 11:04</strong> </span></p>
</div>
</div>
<div id="comments-container-9854" class="comments-container">
<span id="9857"></span>
<div id="comment-9857" class="comment">
<div id="post-9857-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, that explains the CC-BY-SA situation perfectly. ODbL looks like it should be workable, but a close examination is clearly needed. Since Apple may change their terms by April 1st, I think I'll wait until then.</p>
</div>
<div id="comment-9857-info" class="comment-info">
<span class="comment-age">(08 Jan '12, 16:42)</span> <span class="comment-user userinfo">Abhi Beckert</span>
</div>
</div>
</div>
<div id="comment-tools-9854" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9854-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9850"></span>

<div id="answer-container-9850" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9850-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9850-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9850-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Most apps do not contain OSM data, but will download OSM data/maps after installation. In these cases, OSM data is not distributed through Apple's app store at all, and the terms of the app store do not apply to it.</p>
<p>Even distributing OSM data directly packaged with the application will probably be legal with ODbL, as that license allows for Parallel Distribution in section 4.7 b, "Technological measures and additional terms" - <a href="http://wiki.mako.cc/Parallel_Distribution">unlike CC licenses</a>. I'm not sure whether there is actually a conflict between CC BY-SA and Apple's terms, but enforcing that aspect of the CC BY-SA would be rather pointless now with the introduction of the ODbL for OSM data only a few months away.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jan '12, 09:22</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-9850" class="comments-container">
<span id="9853"></span>
<div id="comment-9853" class="comment">
<div id="post-9853-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>More than half the GPS apps currently installed on my iPhone (including OSM based ones) do come with bundled map data. Apple provides unlimited bandwidth hosting on an industry leading CDN for $100 per year, even for free apps that weigh in at several hundred megabytes... quite a bit cheaper than running your own OSM mirror. +1 for mentioning ODbL should fix this, perhaps I'll wait until then before releasing my app.</p>
</div>
<div id="comment-9853-info" class="comment-info">
<span class="comment-age">(08 Jan '12, 10:19)</span> <span class="comment-user userinfo">Abhi Beckert</span>
</div>
</div>
</div>
<div id="comment-tools-9850" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9850-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9848"></span>

<div id="answer-container-9848" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9848-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9848-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9848-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think you are confusing the license for the application with the license for the data. It is only the application itself that has to comply with the App Store terms.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jan '12, 08:39</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-9848" class="comments-container">
<span id="9851"></span>
<div id="comment-9851" class="comment">
<div id="post-9851-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Apple's term is not "application", it's "product". I would read "product" to include any data which comes with the product.</p>
</div>
<div id="comment-9851-info" class="comment-info">
<span class="comment-age">(08 Jan '12, 10:15)</span> <span class="comment-user userinfo">Abhi Beckert</span>
</div>
</div>
</div>
<div id="comment-tools-9848" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9848-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9849"></span>

<div id="answer-container-9849" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9849-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9849-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9849-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have not read the license in question, however if there is no conflicting points (like "This data is property of Apple" or "You may not distribute the data to other parties") you are fine as long as you also publish the data as CC-BY-SA.</p>
<p>The most common is not to include the map in the package that is sold, but to sell a program that downloads an updated dataset from the developers server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jan '12, 08:42</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-9849" class="comments-container">
<span id="9852"></span>
<div id="comment-9852" class="comment">
<div id="post-9852-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>One of the restrictions apple places, is only installing the product on devices that are approved by Apple (see the Pystar lawsuit for an example of how serious they take this), and only on devices you own yourself (you are legally not allowed to send a copy of the app or any of the data bundled with it to your friend, even if it's a free app). In the case of the iOS app store (but not the mac app store) there is also mandatory DRM to enforce this. Downloading the data from a remote server would bypass it I suppose, but many apps don't do that.</p>
</div>
<div id="comment-9852-info" class="comment-info">
<span class="comment-age">(08 Jan '12, 10:17)</span> <span class="comment-user userinfo">Abhi Beckert</span>
</div>
</div>
</div>
<div id="comment-tools-9849" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9849-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

