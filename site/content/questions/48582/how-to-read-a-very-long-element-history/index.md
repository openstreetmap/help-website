+++
type = "question"
title = "How to read a very long element history"
description = '''Some relations can have thousands of revisions and the “View History” link times out. There is a full history dump but it is vastly greater than the history of a single element and takes too much time and space for a home computer or mobile device. Is there a more efficient way to do this, maybe sta...'''
date = "2016-03-08T22:16:00Z"
lastmod = "2016-03-09T10:15:00Z"
weight = 48582
keywords = [ "elements", "relations", "history" ]
aliases = [ "/questions/48582" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to read a very long element history](/questions/48582/how-to-read-a-very-long-element-history)

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
<span id="post-48582-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48582-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48582-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Some relations can have thousands of revisions and the “View History” link times out. There is a <a href="http://wiki.openstreetmap.org/wiki/Planet.osm/full">full history dump</a> but it is vastly greater than the history of a single element and takes too much time and space for a home computer or mobile device.</p>
<p>Is there a more efficient way to do this, maybe starting with the most recent revisions?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-elements" rel="tag" title="see questions tagged &#39;elements&#39;">elements</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Mar '16, 22:16</strong></p>
<img src="https://secure.gravatar.com/avatar/8d2104911958906e2105c27461780d2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wynndale&#39;s gravatar image" />
<p><span>Wynndale</span><br />
<span class="score" title="565 reputation points">565</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wynndale has one accepted answer">7%</span></p>
</div>
</div>
<div id="comments-container-48582" class="comments-container">
&#10;</div>
<div id="comment-tools-48582" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48582-form-container" class="comment-form-container">
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

<span id="48583"></span>

<div id="answer-container-48583" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48583-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48583-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-48583-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You might find osm.mapki.com useful - see for example with <a href="http://osm.mapki.com/history/relation.php?id=357215">this relation</a>. If necessary you can also get individual versions from the API:</p>
<pre><code>wget https://openstreetmap.org/api/0.6/relation/1820890/83</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Mar '16, 22:21</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Mar '16, 22:24</strong> </span></p>
</div>
</div>
<div id="comments-container-48583" class="comments-container">
<span id="48584"></span>
<div id="comment-48584" class="comment">
<div id="post-48584-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also, for objects with ultra long history, I recommend just deleting and re-creating them under a new ID, with an additional tag "note=original object ID was ..." or so. Makes life easier for those that come after you!</p>
</div>
<div id="comment-48584-info" class="comment-info">
<span class="comment-age">(08 Mar '16, 22:31)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48583" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48583-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48590"></span>

<div id="answer-container-48590" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48590-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-48590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One option is to use <a href="http://wiki.openstreetmap.org/wiki/Josm">josm</a> to view the history. Download the location or just the object (file -&gt; download from osm or file -&gt; download object), select the object, and view its history (Ctrl-H or view -&gt; history).</p>
<p>In my experience it's much faster than <a href="http://osm.mapki.com/history/">mapki</a> or even <a href="http://wiki.openstreetmap.org/wiki/OSM_History_Viewer">osmhv</a>, taking 20s to show <a href="http://www.openstreetmap.org/relation/338539">this test relation</a>'s history when the other two timed out on me.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Mar '16, 10:15</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-48590" class="comments-container">
&#10;</div>
<div id="comment-tools-48590" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48590-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48589"></span>

<div id="answer-container-48589" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48589-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48589-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-48589-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Finding those relation versions from the full history dump on your home computer probably doesn't take as much time as you think. With the <a href="https://github.com/osmcode/osmium-tool">osmium command line tool</a> you can easily pick out all the versions of a particular object. For instance reading all versions of the relation id 1820890 took only about 7 minutes on my notebook:</p>
<pre><code>osmium getid history.osm.pbf r1820890 -o /tmp/r1820890-hist.osm.xml</code></pre>
<p>Downloading the full history dump will probably take longer. :-) Make sure to use the PBF version of the history and not the XML version, because parsing it is much faster.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Mar '16, 09:55</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-48589" class="comments-container">
&#10;</div>
<div id="comment-tools-48589" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48589-form-container" class="comment-form-container">
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

