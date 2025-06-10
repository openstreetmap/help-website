+++
type = "question"
title = "Overpass to return entities created &gt; 2 years ago"
description = '''Hi I want to find all landuse=construction entities that were created over 2 years ago. I&#x27;ve looked at diff, adiff, changed etc. OverpassTurbo has &#x27;newer&#x27; but not an equivalent &#x27;older&#x27; it appears. All of these option work with their last modified date but I want it to be based on their created date....'''
date = "2016-12-08T18:40:00Z"
lastmod = "2016-12-09T22:30:00Z"
weight = 53391
keywords = [ "date", "overpass", "created" ]
aliases = [ "/questions/53391" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass to return entities created \> 2 years ago](/questions/53391/overpass-to-return-entities-created-2-years-ago)

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
<span id="post-53391-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53391-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53391-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I want to find all landuse=construction entities that were created over 2 years ago. I've looked at diff, adiff, changed etc. OverpassTurbo has 'newer' but not an equivalent 'older' it appears. All of these option work with their last modified date but I want it to be based on their created date. I'm unable to even find a 'created' attribute in an entities meta data. Does anyone have an example of what I require.</p>
<p>Edit: For clarity, I want to return all existing landuse=construction entities that are older than two years.</p>
<p>Cheers</p>
<p>Dave F.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-date" rel="tag" title="see questions tagged &#39;date&#39;">date</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-created" rel="tag" title="see questions tagged &#39;created&#39;">created</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Dec '16, 18:40</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Dec '16, 11:33</strong> </span></p>
</div>
</div>
<div id="comments-container-53391" class="comments-container">
<span id="53407"></span>
<div id="comment-53407" class="comment">
<div id="post-53407-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You need all versions of an entity?</p>
</div>
<div id="comment-53407-info" class="comment-info">
<span class="comment-age">(09 Dec '16, 00:02)</span> <span class="comment-user userinfo">Wetitpig0</span>
</div>
</div>
<span id="53408"></span>
<div id="comment-53408" class="comment">
<div id="post-53408-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I need landuse=construction entities, within a boundary box, that were created over 2 years ago. I'm not interested in how many times they've been amended.</p>
</div>
<div id="comment-53408-info" class="comment-info">
<span class="comment-age">(09 Dec '16, 00:11)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-53391" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53391-form-container" class="comment-form-container">
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

<span id="53446"></span>

<div id="answer-container-53446" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53446-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53446-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53446-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="DaveF has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can achieve this in several ways with Overpass. For instance the changed predicate.</p>
<p>I have used the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Difference">difference</a> between <strong>all</strong> <code>landuse=construction</code> and <code>landuse=construction</code> <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#newer">newer</a> than a given data. Link to <a href="http://overpass-turbo.eu/s/kyA">query</a>.</p>
<p>Core bits of query (just for ways to keep simple):</p>
<pre><code>{{geocodeArea:Nottingham}}-&gt;.searchArea;
 (way[&quot;landuse&quot;=&quot;construction&quot;](area.searchArea)
  -
  way._(newer:&quot;2014-12-14T07:00:00Z&quot;)[&quot;landuse&quot;=&quot;construction&quot;](area.searchArea);)</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Dec '16, 22:30</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-53446" class="comments-container">
&#10;</div>
<div id="comment-tools-53446" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53446-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53414"></span>

<div id="answer-container-53414" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53414-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not exactly "before 2 years ago", but <a href="http://overpass-turbo.eu/s/kxm">here</a> is one "at a particular date, which can be 2 years ago". Depending on what you're looking for, that might work.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Dec '16, 01:19</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-53414" class="comments-container">
<span id="53440"></span>
<div id="comment-53440" class="comment">
<div id="post-53440-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. I looked at 'date' but it appears to also return all entities which <em>were</em> landuse=construction, but have since had their tags amended. It also only goes back to 2012, which will not be far enough back in time for my future requirements. IMO 'date' is to generic a term. It should be more specific for it's detailed purpose. I've just checked: 'date' returns completely deleted entities. It definitely should be renamed.</p>
</div>
<div id="comment-53440-info" class="comment-info">
<span class="comment-age">(09 Dec '16, 11:29)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="53441"></span>
<div id="comment-53441" class="comment">
<div id="post-53441-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you want pre licence-change data, you're probably going to need to handle the old planet files yourself.</p>
<p>With regard to "date" it's returning "the situation as of that date" - looks like it does what it says on the tin to me.</p>
</div>
<div id="comment-53441-info" class="comment-info">
<span class="comment-age">(09 Dec '16, 12:16)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-53414" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53414-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53409"></span>

<div id="answer-container-53409" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53409-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First filter a full-history file with <a href="https://wiki.openstreetmap.org/wiki/Osmfilter#Object_Filter">osmfilter</a>, then choose select all within 2 years with <a href="http://docs.osmcode.org/osmium/latest/osmium-time-filter.html">Osmium</a>. But all change versions will be kept.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Dec '16, 00:41</strong></p>
<img src="https://secure.gravatar.com/avatar/100f8ccde5e9799707a5056f94fe183f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wetitpig0&#39;s gravatar image" />
<p><span>Wetitpig0</span><br />
<span class="score" title="307 reputation points">307</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wetitpig0 has 2 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-53409" class="comments-container">
<span id="53411"></span>
<div id="comment-53411" class="comment">
<div id="post-53411-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I wish to use Overpass api or Preferably Overpass Turbo.</p>
</div>
<div id="comment-53411-info" class="comment-info">
<span class="comment-age">(09 Dec '16, 00:50)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="53412"></span>
<div id="comment-53412" class="comment">
<div id="post-53412-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If they don't provide it you do not have any choice.</p>
</div>
<div id="comment-53412-info" class="comment-info">
<span class="comment-age">(09 Dec '16, 01:04)</span> <span class="comment-user userinfo">Wetitpig0</span>
</div>
</div>
<span id="53413"></span>
<div id="comment-53413" class="comment">
<div id="post-53413-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have never used Overpass API</p>
</div>
<div id="comment-53413-info" class="comment-info">
<span class="comment-age">(09 Dec '16, 01:05)</span> <span class="comment-user userinfo">Wetitpig0</span>
</div>
</div>
<span id="53439"></span>
<div id="comment-53439" class="comment">
<div id="post-53439-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Err... I'm unsure if they provide it, which is why I'm asking.</p>
</div>
<div id="comment-53439-info" class="comment-info">
<span class="comment-age">(09 Dec '16, 11:16)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-53409" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53409-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53442"></span>

<div id="answer-container-53442" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53442-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53442-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53442-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If "I want to find all landuse=construction entities that were created over 2 years ago" means "I want to find all landuse=construction entities THAT STILL EXIST that were created over 2 years ago" then it's actually much easier. do a binary chop in the node, way and relation list to find roughly the date that you're interested in, and search for nodes, ways and relations with ids less than that.</p>
<p>That's probably doable with Overpass et al, and I'm sure that some of the links from <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo/Examples">here</a> will explain how.</p>
<p>Obviously this doesn't solve the "object X was issued a new id Y during editing", but it'll get most of what you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Dec '16, 12:22</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-53442" class="comments-container">
&#10;</div>
<div id="comment-tools-53442" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53442-form-container" class="comment-form-container">
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

