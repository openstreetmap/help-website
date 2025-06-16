+++
type = "question"
title = "Adding large number of points"
description = '''I have recently found out that the transit authority in my area publishes transit information for download for app developers. This includes various transit stops (mostly bus and light rail), including longitude, latitude, stop IDs, stop names, and bus routes that visit each route. I&#x27;d like to be ab...'''
date = "2015-03-13T22:57:00Z"
lastmod = "2015-03-16T16:34:00Z"
weight = 41692
keywords = [ "editing", "public-transport", "public_transport" ]
aliases = [ "/questions/41692" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Adding large number of points](/questions/41692/adding-large-number-of-points)

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
<span id="post-41692-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41692-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-41692-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have recently found out that the transit authority in my area publishes transit information for download for app developers. This includes various transit stops (mostly bus and light rail), including longitude, latitude, stop IDs, stop names, and bus routes that visit each route. I'd like to be able to add these to OSM, but there's one big problem: there are just under <em>7000</em> points to add, and as far as I can find they don't publish in a format that I could import into OSM without some sort of conversion of database formats.</p>
<p>Given that one of the database files provided by the transit authority can be opened as a spreadsheet that I can view/edit from OpenOffice/LibreOffice Calc, would there be a simple way of importing these into OSM (from Linux)? I wouldn't mind doing a little work if it means making sure I don't accidentally corrupt the OSM database, but adding nearly 7000 points to the map would be much too tedious for one person.</p>
<p>(for those interested, the data is at <a href="http://www.portauthority.org/generaltransitfeed/GIS/" title="http://www.portauthority.org/generaltransitfeed/GIS/">http://www.portauthority.org/generaltransitfeed/GIS/</a> , they pack several database formats in the zip files)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-public-transport" rel="tag" title="see questions tagged &#39;public-transport&#39;">public-transport</span> <span class="post-tag tag-link-public_transport" rel="tag" title="see questions tagged &#39;public_transport&#39;">public_transport</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Mar '15, 22:57</strong></p>
<img src="https://secure.gravatar.com/avatar/472d9e4d016f569f2306330e88532c33?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ItchyDemon&#39;s gravatar image" />
<p><span>ItchyDemon</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ItchyDemon has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Mar '15, 22:59</strong> </span></p>
</div>
</div>
<div id="comments-container-41692" class="comments-container">
<span id="41696"></span>
<div id="comment-41696" class="comment">
<div id="post-41696-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Note that there are already a number of bus stops in the area already:</p>
<p><a href="http://overpass-turbo.eu/s/8bg">http://overpass-turbo.eu/s/8bg</a></p>
<p>(not 7000, but some).</p>
</div>
<div id="comment-41696-info" class="comment-info">
<span class="comment-age">(14 Mar '15, 00:09)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="41697"></span>
<div id="comment-41697" class="comment">
<div id="post-41697-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sure, and I'm responsible for a few of them being on the map :-)</p>
<p>I figure the number of bus stops on the map are problem not more than a few hundred, and compared to nearly 7000 it would probably be easier to seek out and merge/remove duplicates than add a few thousand individually.</p>
</div>
<div id="comment-41697-info" class="comment-info">
<span class="comment-age">(14 Mar '15, 00:13)</span> <span class="comment-user userinfo">ItchyDemon</span>
</div>
</div>
<span id="41698"></span>
<div id="comment-41698" class="comment">
<div id="post-41698-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry for the typo -- I meant "probably not more than".</p>
</div>
<div id="comment-41698-info" class="comment-info">
<span class="comment-age">(14 Mar '15, 00:23)</span> <span class="comment-user userinfo">ItchyDemon</span>
</div>
</div>
</div>
<div id="comment-tools-41692" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41692-form-container" class="comment-form-container">
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

<span id="41719"></span>

<div id="answer-container-41719" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41719-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41719-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-41719-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sorry, the <a href="http://www.portauthority.org/paac/CompanyInfoProjects/DeveloperResources/DeveloperLicenseAgreement.aspx">licence for that data</a> does not seem compatible with <a href="https://www.openstreetmap.org/copyright">OSM's licence</a>. IANAL and I did not read through everything, but at least paragraphs 2, 4, and 6 seem clearly incompatible with OSM/ODBL. As it stands, <em>you cannot import this data into OSM</em>.</p>
<p>However, it is certainly worth it to contact the owner of the data to see if they are willing to either relicense their data in an odbl-compatible way, or to grant an official, writen exception for OSM to import the data. Alert them to the fact that providing "open" data that can only be used in very restricted circumstances is rather pointless. How easy they are to convince depends on your luck, but sending a few emails is worth it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Mar '15, 21:10</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-41719" class="comments-container">
<span id="41722"></span>
<div id="comment-41722" class="comment">
<div id="post-41722-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Way ahead of you on that -- after reading the wiki link from the answer above yours (which mentions the license thing), I when searching through their site and found their license. I've already submitted a message through their feedback form suggesting that they add their stops themselves. If they don't respond within the next week or two, I'll probably send them a letter asking them to either add the stops or grant me permission to do so.</p>
</div>
<div id="comment-41722-info" class="comment-info">
<span class="comment-age">(15 Mar '15, 21:23)</span> <span class="comment-user userinfo">ItchyDemon</span>
</div>
</div>
<span id="41723"></span>
<div id="comment-41723" class="comment">
<div id="post-41723-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Good :) Just wanted to make sure the license issue was known, in case you had just skimed over the guidelines but figured out the technical part anyway.</p>
</div>
<div id="comment-41723-info" class="comment-info">
<span class="comment-age">(15 Mar '15, 21:52)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="41745"></span>
<div id="comment-41745" class="comment">
<div id="post-41745-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>IANAL, but since the Port Authority's a government agency, <a href="http://www.rcfp.org/pennsylvania-open-government-guide/i-statute-basic-application/b-whose-records-are-and-are-not-subje">http://www.rcfp.org/pennsylvania-open-government-guide/i-statute-basic-application/b-whose-records-are-and-are-not-subje</a> seems to suggest that their license doesn't comply with state law.</p>
</div>
<div id="comment-41745-info" class="comment-info">
<span class="comment-age">(16 Mar '15, 16:34)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-41719" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41719-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41693"></span>

<div id="answer-container-41693" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41693-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41693-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-41693-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi ItchyDemon, before answering your question, please read these lines and follow the import rules accordingly, <a href="https://wiki.openstreetmap.org/wiki/Import/Guidelines">https://wiki.openstreetmap.org/wiki/Import/Guidelines</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Mar '15, 23:23</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Mar '15, 00:04</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-41693" class="comments-container">
<span id="41694"></span>
<div id="comment-41694" class="comment">
<div id="post-41694-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Um, there's a big problem with that... The link you provide gives the following messages from the OSM wiki:</p>
<p>There is currently no text in this page. You can search for this page title in other pages, or search the related logs, but you do not have permission to create this page.</p>
</div>
<div id="comment-41694-info" class="comment-info">
<span class="comment-age">(13 Mar '15, 23:53)</span> <span class="comment-user userinfo">ItchyDemon</span>
</div>
</div>
<span id="41695"></span>
<div id="comment-41695" class="comment">
<div id="post-41695-score" class="comment-score">
5
</div>
<div class="comment-text">
<p>For info - I fixed the broken link in the answer above.</p>
</div>
<div id="comment-41695-info" class="comment-info">
<span class="comment-age">(14 Mar '15, 00:05)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41693" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41693-form-container" class="comment-form-container">
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

