+++
type = "question"
title = "I&#x27;m trying to download the internal boundaries of nearly each country and facing runtime errors."
description = '''I&#x27;m facing runtime errors for big countries and if it succeeds the browser crashes. I&#x27;m actually using this qeury in a python script [out:json][timeout:350];  area(3600365331)-&amp;gt;.searchArea;  (  way[&quot;boundary&quot;=&quot;administrative&quot;](area.searchArea);  relation[&quot;boundary&quot;=&quot;administrative&quot;](area.searchAr...'''
date = "2021-06-23T09:00:00Z"
lastmod = "2021-06-24T14:44:00Z"
weight = 80669
keywords = [ "overpass", "nominatim", "overpass-turbo", "osm", "query" ]
aliases = [ "/questions/80669" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [I'm trying to download the internal boundaries of nearly each country and facing runtime errors.](/questions/80669/im-trying-to-download-the-internal-boundaries-of-nearly-each-country-and-facing-runtime-errors)

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
<span id="post-80669-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80669-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80669-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm facing runtime errors for big countries and if it succeeds the browser crashes. I'm actually using this qeury in a python script</p>
<pre><code>[out:json][timeout:350];
    area(3600365331)-&gt;.searchArea;
    (
      way[&quot;boundary&quot;=&quot;administrative&quot;](area.searchArea);
      relation[&quot;boundary&quot;=&quot;administrative&quot;](area.searchArea);
    );
     (._;&gt;;);out body;</code></pre>
<p>Is there anything I'm doing wrong ? or is there any better query for what I want ? <a href="https://drive.google.com/file/d/1WGWKxXpW3s0xee-JU2E_9rXL_5vAxIZo/view?usp=sharing">https://drive.google.com/file/d/1WGWKxXpW3s0xee-JU2E_9rXL_5vAxIZo/view?usp=sharing</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jun '21, 09:00</strong></p>
<img src="https://secure.gravatar.com/avatar/37064a4c6737277dbdc244fd3fdd108e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jad&#39;s gravatar image" />
<p><span>Jad</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jad has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jun '21, 16:58</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span></p>
</div>
</div>
<div id="comments-container-80669" class="comments-container">
<span id="80671"></span>
<div id="comment-80671" class="comment">
<div id="post-80671-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://drive.google.com/file/d/1WGWKxXpW3s0xee-JU2E_9rXL_5vAxIZo/view?usp=sharing">https://drive.google.com/file/d/1WGWKxXpW3s0xee-JU2E_9rXL_5vAxIZo/view?usp=sharing</a> This is an instance</p>
</div>
<div id="comment-80671-info" class="comment-info">
<span class="comment-age">(23 Jun '21, 09:02)</span> <span class="comment-user userinfo">Jad</span>
</div>
</div>
</div>
<div id="comment-tools-80669" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80669-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="80673"></span>

<div id="answer-container-80673" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80673-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-80673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at <a href="https://osm-boundaries.com/">https://osm-boundaries.com/</a> On the left-hand side in the country structure you can right-click and select all children (or only those you need). After clicking the download button you'll be asked which data format you require.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jun '21, 11:19</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-80673" class="comments-container">
&#10;</div>
<div id="comment-tools-80673" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80673-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="80683"></span>

<div id="answer-container-80683" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80683-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80683-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80683-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello.</p>
<p>Boundaries <strong>are</strong> huge, thus I think mtmail's answer is probably the best way.</p>
<p>But if you really need to go through overpass, first you should simplify your request. You don't need to ask for the ways, as they will be children of the relation. That should lighten the burden of the server if you don't ask the same objects twice.</p>
<p>Then, the search area is not precise enough, in your example (targeting Italy) I got the whole boundary of France and some of its regions. Maybe "is_in" might be better.</p>
<p>Also, do you really need every kind of boundaries there is ? National parks, municipality, voting zones, and so on. Maybe you could filter with admin_level. Trouble is that it's not totally consistent across every country, but I think it's thoroughly documented in the wiki (<a href="https://wiki.openstreetmap.org/wiki/Key:boundary">boundary</a>, <a href="https://wiki.openstreetmap.org/wiki/Key:admin_level">admin_level</a> and subpages).</p>
<p>Good luck.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jun '21, 11:05</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-80683" class="comments-container">
&#10;</div>
<div id="comment-tools-80683" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80683-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="80688"></span>

<div id="answer-container-80688" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80688-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First, a general point: Could contributors, other than the OP, not alter the original question. It can make any replies appear to be nonsense &amp; confuse those trying to learn. A part of Jad's problem was the syntax of the code. To correct it, an Answer should have been provided.</p>
<p>There are two answers to this Q</p>
<p>1) As as <a href="https://help.openstreetmap.org/users/150/mtmail">@mtmail</a> suggests use the boundary site, where they have already been saved &amp; segregated off the main server.</p>
<p>2) Going on JAD's original code as posted, the routine wouldn't have run, &amp; even when corrected would probably have timed out for the whole of Italy.</p>
<p>This adapted routine is restricted to the visible area &amp; to boundaries of only one admin level: <a href="https://overpass-turbo.eu/s/18Nl">https://overpass-turbo.eu/s/18Nl</a></p>
<pre><code>[bbox:{{bbox}}];
rel[boundary=administrative][admin_level=4];
out geom;</code></pre>
<p>There is no need to search for boundary <code>ways</code> as all should be mapped as <code>rels</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jun '21, 13:34</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-80688" class="comments-container">
<span id="80689"></span>
<div id="comment-80689" class="comment">
<div id="post-80689-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Dave. I merely formatted the query as code (with the grey background) as it was displayed as a single long line before. I didn't alter it in any way. And I shortened the title which ran over several lines and put the question in the text instead. Both served to make the question better readable but I didn't change anything in the content.</p>
</div>
<div id="comment-80689-info" class="comment-info">
<span class="comment-age">(24 Jun '21, 14:44)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-80688" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80688-form-container" class="comment-form-container">
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

