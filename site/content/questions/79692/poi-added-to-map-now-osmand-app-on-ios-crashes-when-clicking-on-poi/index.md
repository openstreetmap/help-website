+++
type = "question"
title = "POI added to Map, now OSMand App on iOS crashes when clicking on POI"
description = '''Hi, I added a business to a point (Node: Hairgalerie Friseur (2399202263)). I saw the edit correctly in the OsmAnd app in iOS. But when I clicked on it, the app crashed. I had omitted the http in front of the web address, thought this might be the error, edited the tag, but still, whenever I navigat...'''
date = "2021-04-17T13:16:00Z"
lastmod = "2021-04-19T20:33:00Z"
weight = 79692
keywords = [ "poi" ]
aliases = [ "/questions/79692" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [POI added to Map, now OSMand App on iOS crashes when clicking on POI](/questions/79692/poi-added-to-map-now-osmand-app-on-ios-crashes-when-clicking-on-poi)

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
<span id="post-79692-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79692-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79692-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I added a business to a point (Node: Hairgalerie Friseur (2399202263)). I saw the edit correctly in the OsmAnd app in iOS. But when I clicked on it, the app crashed. I had omitted the http in front of the web address, thought this might be the error, edited the tag, but still, whenever I navigate to the hairdresser, I see the POI, click on it, and my app crashes. This happends both on iPhone and iPad. However, when I look at the streetmap data on my iMac in Safari, I do not even see the POI I created. Only when I log in as if to edit. No idea what caused this. Any advice? <a href="https://www.openstreetmap.org/node/2399202263">https://www.openstreetmap.org/node/2399202263</a> Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Apr '21, 13:16</strong></p>
<img src="https://secure.gravatar.com/avatar/8a2dbe07ef1b3ce7f3c6d0dc121595d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Monterossa&#39;s gravatar image" />
<p><span>Monterossa</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Monterossa has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Apr '21, 10:35</strong> </span></p>
</div>
</div>
<div id="comments-container-79692" class="comments-container">
<span id="79734"></span>
<div id="comment-79734" class="comment">
<div id="post-79734-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for the answers. I deleted the POI and started again. Now with the correct syntax for opening hours and phone number. New node: <a href="https://www.openstreetmap.org/node/8643108836">https://www.openstreetmap.org/node/8643108836</a></p>
<p>I can now see it in Safari on my iMac by changing zoom levels.</p>
<p>On iPhone and iPad, using OsmAnd app (latest version) and after I updated the map data, it still crashes the app when clicking on the POI.</p>
<p>I compared my entry in html code and that of a nearby restaurant. No difference in syntax.</p>
<p>I did write a bug report on GitHub as suggested.</p>
</div>
<div id="comment-79734-info" class="comment-info">
<span class="comment-age">(19 Apr '21, 12:03)</span> <span class="comment-user userinfo">Monterossa</span>
</div>
</div>
<span id="79737"></span>
<div id="comment-79737" class="comment">
<div id="post-79737-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Do you use OsmAnd Live ? Otherwise the data are only updated at the start of every month.</p>
<p>And the <a href="https://wiki.openstreetmap.org/wiki/Key:opening_hours">opening_hours</a> looks better, but days abbreviations are still not in English. It should not make the app crash, but it is still wrong, and probably not understood by most software.</p>
<p>You should really try yohours (or others) to build your opening_hours, it's quite tricky to get right.</p>
<p>Regards.</p>
</div>
<div id="comment-79737-info" class="comment-info">
<span class="comment-age">(19 Apr '21, 13:24)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="79749"></span>
<div id="comment-79749" class="comment">
<div id="post-79749-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You are absolutely correct. Now with correct opening hours set, the OsmAnd Apps no longer crash and data is shown correctly.</p>
</div>
<div id="comment-79749-info" class="comment-info">
<span class="comment-age">(19 Apr '21, 20:33)</span> <span class="comment-user userinfo">Monterossa</span>
</div>
</div>
</div>
<div id="comment-tools-79692" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79692-form-container" class="comment-form-container">
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

<span id="79702"></span>

<div id="answer-container-79702" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79702-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79702-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-79702-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Monterossa has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For the "not visible in browser", for me it depends on the zoom level, so I guess it's just a problem of cache and rendering delays. Try again tomorrow, after a Ctrl+Shift+R if necessary, it should display alright.</p>
<p>For the trouble in iOS, I don't get what app you are using. Are you sure the data is updated on the fly ? For example I use OsmAnd on Android, and I download the data updated only every month...</p>
<p>But by looking at your edit, I don't think the <a href="https://wiki.openstreetmap.org/wiki/Key:opening_hours">opening_hours</a> value is valid. The syntax is quite strict, and only English abbreviations are used I think. Check the wiki. There are web tools to check the syntax, or even to build it graphically, like <a href="https://projets.pavie.info/yohours/">yohours</a>. Maybe the crash comes from that. You should tell the developers of your app that it should fail silently when the opening_hours values are not correct, because it happens quite often.</p>
<p>And the <a href="https://wiki.openstreetmap.org/wiki/Key:phone">phone</a> value should be in international format (like +xx...), but I really don't think that's the issue with your app. ;-)</p>
<p>In any case, thanks for your edits. :-) I go to the wiki for nearly every tag, at least the first time I use them. And some (like opening_hours), nearly every time. Quite a lot of reading at first, but you'll get more efficient after a little while.</p>
<p>Also JOSM is a bit more difficult at first, but you really understand what is going on with the data, unlike iD.</p>
<p>My 2 cents.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Apr '21, 16:59</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-79702" class="comments-container">
&#10;</div>
<div id="comment-tools-79702" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79702-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="79729"></span>

<div id="answer-container-79729" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79729-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79729-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-79729-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If OsmAnd iOS crashes then this is the fault of the app. You can create a bug report here: <a href="https://github.com/osmandapp/OsmAnd-iOS/issues">https://github.com/osmandapp/OsmAnd-iOS/issues</a>. It needs a GitHub account.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Apr '21, 07:13</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Apr '21, 08:18</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span></p>
</div>
</div>
<div id="comments-container-79729" class="comments-container">
&#10;</div>
<div id="comment-tools-79729" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79729-form-container" class="comment-form-container">
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

