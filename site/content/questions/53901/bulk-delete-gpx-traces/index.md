+++
type = "question"
title = "Bulk delete gpx traces?"
description = '''Hi  I want to delete my own older GPX traces, There&#x27;s quire a lot of them. Is there a way to delete them in one go?'''
date = "2017-01-07T13:26:00Z"
lastmod = "2018-04-25T09:50:00Z"
weight = 53901
keywords = [ "gpx", "delete" ]
aliases = [ "/questions/53901" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Bulk delete gpx traces?](/questions/53901/bulk-delete-gpx-traces)

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
<span id="post-53901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53901-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-53901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I want to delete my own older GPX traces, There's quire a lot of them. Is there a way to delete them in one go?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-delete" rel="tag" title="see questions tagged &#39;delete&#39;">delete</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jan '17, 13:26</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-53901" class="comments-container">
<span id="54140"></span>
<div id="comment-54140" class="comment">
<div id="post-54140-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As an aside, it might be worth asking "delete from where". For example, I suspect that a delete of a trace from OSM won't remove it from the trace layer that iD uses (see <a href="https://github.com/ericfischer/gpx-updater/issues/1">https://github.com/ericfischer/gpx-updater/issues/1</a> and the links from that). I'm not sure what P2 or JOSM do; <a href="https://github.com/openstreetmap/iD/issues/2450">https://github.com/openstreetmap/iD/issues/2450</a> says that the GPX API is "agonizingly slow" so I don't know if there is any intermediate state there.</p>
</div>
<div id="comment-54140-info" class="comment-info">
<span class="comment-age">(18 Jan '17, 13:17)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63122"></span>
<div id="comment-63122" class="comment">
<div id="post-63122-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>2 days ago I had a comparable issue. I accidentally uploaded a bunch of unusable GPXs due to a wrong auto-upload setting in my device. It would be nice to have a bulk-delete feature. Now I deleted them individually as they were only 30, fortunately.</p>
</div>
<div id="comment-63122-info" class="comment-info">
<span class="comment-age">(25 Apr '18, 09:50)</span> <span class="comment-user userinfo">emNowak</span>
</div>
</div>
</div>
<div id="comment-tools-53901" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53901-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="53905"></span>

<div id="answer-container-53905" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53905-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The answer is "no", and given there is no API call to delete even a single one, it is currently not possible to "roll your own" in any reasonable fashion either.</p>
<p>Naturally your question raises the question why you would want to delete "older GPX traces" to start with?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jan '17, 16:32</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jan '17, 16:35</strong> </span></p>
</div>
</div>
<div id="comments-container-53905" class="comments-container">
<span id="53906"></span>
<div id="comment-53906" class="comment">
<div id="post-53906-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>One reason might be somthing like the 18 second time lag I experience. GPX: My Tracks: fetching tracks, i experience waiting for fetching of the tracks choice to appear in Potlatch2. But there are over 900 now.</p>
</div>
<div id="comment-53906-info" class="comment-info">
<span class="comment-age">(07 Jan '17, 16:45)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="53907"></span>
<div id="comment-53907" class="comment">
<div id="post-53907-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But i would rather they are available for future editing and reference.</p>
</div>
<div id="comment-53907-info" class="comment-info">
<span class="comment-age">(07 Jan '17, 16:48)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="53909"></span>
<div id="comment-53909" class="comment">
<div id="post-53909-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>and according to <a href="http://hdyc.neis-one.org/">http://hdyc.neis-one.org/</a> DaveF seems to use Potlatch2 and as uploaded almost 500 traces.</p>
</div>
<div id="comment-53909-info" class="comment-info">
<span class="comment-age">(07 Jan '17, 17:58)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="54126"></span>
<div id="comment-54126" class="comment">
<div id="post-54126-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are a few reasons. Does the OSM 'traces' webpage not delete a GPX with an API call? As Andy indicates it's possible to see about a contributor's contributions. I'm surprised there's no way to delete.</p>
</div>
<div id="comment-54126-info" class="comment-info">
<span class="comment-age">(18 Jan '17, 02:02)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="54130"></span>
<div id="comment-54130" class="comment">
<div id="post-54130-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I haven't directly checked the code, just the API, but the Rails port will likely simply remove the entry "directly" from the database. IMHO the way forward would be to address any performance issues not to start deleting tracks in a larger way.</p>
</div>
<div id="comment-54130-info" class="comment-info">
<span class="comment-age">(18 Jan '17, 08:37)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-53905" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53905-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="54131"></span>

<div id="answer-container-54131" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54131-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you had uploaded a trace in error Admin may be able to help you. I guess traces aren't easily deletable as they are a witness to your survey. A mapping company could contest copyright and OSM could use the traces as evidence of our survey. Traces are is less important (as a witness) now we have good Ariel available but are needed to check alignment. It is sensible to review any trace before we upload them as they may show your home or another private area. I use GPS Prune to see the trace on OSM and then trim of any excess i don't wish to upload.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jan '17, 08:48</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jan '17, 10:51</strong> </span></p>
</div>
</div>
<div id="comments-container-54131" class="comments-container">
<span id="54138"></span>
<div id="comment-54138" class="comment">
<div id="post-54138-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's possible to delete individual traces quite easily. Very few changesets are based on traces so claiming they're needed for evidence is hardly essential. Please note it's my "older" traces I wish to remove. The ones created using old, inaccurate GPS chips, producing erroneous, confusing traces. There are other reasons I wish to remove <em>old</em> traces.</p>
</div>
<div id="comment-54138-info" class="comment-info">
<span class="comment-age">(18 Jan '17, 12:22)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-54131" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54131-form-container" class="comment-form-container">
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

