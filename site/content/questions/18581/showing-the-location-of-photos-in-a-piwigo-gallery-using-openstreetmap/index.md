+++
type = "question"
title = "Showing the location of photos in a Piwigo gallery using OpenStreetMap"
description = '''I just set up a Piwigo (http://piwigo.org/) instance on my shared server account to store photos with. I really would like the ability to show viewers on a map where the photos were taken. Piwigo has extensions that use Bing (http://piwigo.org/ext/extension_view.php?eid=603) and Google (http://piwig...'''
date = "2012-12-18T23:07:00Z"
lastmod = "2012-12-19T22:58:00Z"
weight = 18581
keywords = [ "photos", "piwigo" ]
aliases = [ "/questions/18581" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Showing the location of photos in a Piwigo gallery using OpenStreetMap](/questions/18581/showing-the-location-of-photos-in-a-piwigo-gallery-using-openstreetmap)

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
<span id="post-18581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18581-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I just set up a Piwigo (<a href="http://piwigo.org/)">http://piwigo.org/)</a> instance on my shared server account to store photos with. I really would like the ability to show viewers on a map where the photos were taken. Piwigo has extensions that use Bing (<a href="http://piwigo.org/ext/extension_view.php?eid=603)">http://piwigo.org/ext/extension_view.php?eid=603)</a> and Google (<a href="http://piwigo.org/ext/extension_view.php?eid=122)">http://piwigo.org/ext/extension_view.php?eid=122)</a> but I was wondering how I could use OpenStreetMap or OpenStreetMap data to do something similar.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-photos" rel="tag" title="see questions tagged &#39;photos&#39;">photos</span> <span class="post-tag tag-link-piwigo" rel="tag" title="see questions tagged &#39;piwigo&#39;">piwigo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Dec '12, 23:07</strong></p>
<img src="https://secure.gravatar.com/avatar/5de36e49e2bfcdc9c5548ac4d50a673a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="XinJeisan&#39;s gravatar image" />
<p><span>XinJeisan</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="XinJeisan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18581" class="comments-container">
&#10;</div>
<div id="comment-tools-18581" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18581-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="18641"></span>

<div id="answer-container-18641" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18641-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-18641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In principle there is no problem using the tiles served by OSM as a background on a low volume site, you will naturally need to provide attribution (see <a href="http://www.openstreetmap.org/copyright">http://www.openstreetmap.org/copyright</a> ). If you expect more than a trivial amount of traffic you should either arrange for such a service from a commercial map tile provider or set up your own tile server (see <a href="http://switch2osm.org">switch2osm.org</a> ).</p>
<p>To actually display the tiles you will need to code or extend a Piwigo plugin, but I suspect that you can reuse code from either the google or bing one.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Dec '12, 22:58</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Dec '12, 12:59</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-18641" class="comments-container">
&#10;</div>
<div id="comment-tools-18641" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18641-form-container" class="comment-form-container">
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

