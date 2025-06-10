+++
type = "question"
title = "Map key unclear"
description = '''Hi, on the key a small blue square indicates a railway station, however on the map of where I live (Hucknall, Notts) they appear to have been used to mark bus stops. Should the description on the key be changed? Regards Guy'''
date = "2012-02-21T08:38:00Z"
lastmod = "2012-02-24T13:13:00Z"
weight = 10689
keywords = [ "bus", "proposal", "stops" ]
aliases = [ "/questions/10689" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Map key unclear](/questions/10689/map-key-unclear)

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
<span id="post-10689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10689-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-10689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, on the key a small blue square indicates a railway station, however on the map of where I live (Hucknall, Notts) they appear to have been used to mark bus stops. Should the description on the key be changed?</p>
<p>Regards Guy</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-proposal" rel="tag" title="see questions tagged &#39;proposal&#39;">proposal</span> <span class="post-tag tag-link-stops" rel="tag" title="see questions tagged &#39;stops&#39;">stops</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Feb '12, 08:38</strong></p>
<img src="https://secure.gravatar.com/avatar/f0e93a75c68ad285b53959f58a6cf2dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NottsGuy&#39;s gravatar image" />
<p><span>NottsGuy</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NottsGuy has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Feb '12, 14:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/7d327873d48d28e563c9ad7259853c35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kozuch&#39;s gravatar image" />
<p><span>Kozuch</span><br />
<span class="score" title="1720 reputation points"><span>1.7k</span></span><span title="58 badges"><span class="badge1">●</span><span class="badgecount">58</span></span><span title="72 badges"><span class="silver">●</span><span class="badgecount">72</span></span><span title="85 badges"><span class="bronze">●</span><span class="badgecount">85</span></span></p>
</div>
</div>
<div id="comments-container-10689" class="comments-container">
&#10;</div>
<div id="comment-tools-10689" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10689-form-container" class="comment-form-container">
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

<span id="10764"></span>

<div id="answer-container-10764" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10764-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10764-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-10764-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think the main online map legend could be improved. The small blue square is used for both, railway station and bus stops but the "map key" only indicates the railway station. The text and image of the site map keys seems to be configured in this file: <a href="http://git.openstreetmap.org/rails.git/blob/8c4419412f1edfdb2c0cd282c01b90044dc9116e:/config/locales/en.yml">http://git.openstreetmap.org/rails.git/blob/8c4419412f1edfdb2c0cd282c01b90044dc9116e:/config/locales/en.yml</a></p>
<p>Anyone who can access this file could improve the section:<br />
  station: "Railway station"<br />
by:<br />
  station: "Railway,bus station"</p>
<p>for instance.</p>
<p>If the symbol is not exactly the same, then a new entry could be added in the map key table (I guess it is in the file <a href="http://git.openstreetmap.org/rails.git/blob/8c4419412f1edfdb2c0cd282c01b90044dc9116e:/config/key.yml">http://git.openstreetmap.org/rails.git/blob/8c4419412f1edfdb2c0cd282c01b90044dc9116e:/config/key.yml</a>) and its name (e.g. bus_station) added as well in the internationalisation file referenced above (config/locales/en.yml).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Feb '12, 12:50</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Feb '12, 15:15</strong> </span></p>
</div>
</div>
<div id="comments-container-10764" class="comments-container">
<span id="10768"></span>
<div id="comment-10768" class="comment">
<div id="post-10768-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>They are not exactly the same icon. The railway station symbol seems to be a darker grey/blue colour. Plus the railway station is a bit larger. Though yes, the map key could be clearer.</p>
</div>
<div id="comment-10768-info" class="comment-info">
<span class="comment-age">(24 Feb '12, 13:13)</span> <span class="comment-user userinfo">Vclaw</span>
</div>
</div>
</div>
<div id="comment-tools-10764" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10764-form-container" class="comment-form-container">
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

