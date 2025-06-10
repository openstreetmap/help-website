+++
type = "question"
title = "My map goes blank randomly on and off.  Is this because I hit an upper limit?"
description = '''I have a map on the homepage of my website that goes blank occasionally and I don&#x27;t know what is triggering it to do so. Strangely enough when I login as a user/admin, the map displays fine. I have under 10K hits a month, which only a fraction go to the homepage, so I&#x27;m not sure what kind of limit I...'''
date = "2013-11-03T16:44:00Z"
lastmod = "2013-11-06T08:03:00Z"
weight = 27760
keywords = [ "dissapear", "blank" ]
aliases = [ "/questions/27760" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [My map goes blank randomly on and off. Is this because I hit an upper limit?](/questions/27760/my-map-goes-blank-randomly-on-and-off-is-this-because-i-hit-an-upper-limit)

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
<span id="post-27760-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27760-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27760-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a map on the homepage of my website that goes blank occasionally and I don't know what is triggering it to do so. Strangely enough when I login as a user/admin, the map displays fine. I have under 10K hits a month, which only a fraction go to the homepage, so I'm not sure what kind of limit I would be hitting.<br />
</p>
<p>Anyone else experiencing the same issue or have any suggestions?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-dissapear" rel="tag" title="see questions tagged &#39;dissapear&#39;">dissapear</span> <span class="post-tag tag-link-blank" rel="tag" title="see questions tagged &#39;blank&#39;">blank</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Nov '13, 16:44</strong></p>
<img src="https://secure.gravatar.com/avatar/48cccd070ffc9268266a43ac0ba85552?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nyancat&#39;s gravatar image" />
<p><span>nyancat</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nyancat has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-27760" class="comments-container">
<span id="27761"></span>
<div id="comment-27761" class="comment">
<div id="post-27761-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Please tell some more technical details, it looks like it’s more a server than an OSM problem.</p>
</div>
<div id="comment-27761-info" class="comment-info">
<span class="comment-age">(03 Nov '13, 16:52)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="27762"></span>
<div id="comment-27762" class="comment">
<div id="post-27762-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>your login should not change anything of the map embedding, does it? I guess in both cases you call <a href="http://b.tile.openstreetmap.org/12/2204/1371.png">osm.org tiles</a> (I am assuming you are using those). If you still can access these tiles the problem should not be a <span>Tile usage policy</span>-based block. In addition a block seems to deliver no blank but error tiles.</p>
<p>As Hendrik says, please describe your technical details (link?). And tell us why you think it is a OSM (server) problem.</p>
</div>
<div id="comment-27762-info" class="comment-info">
<span class="comment-age">(03 Nov '13, 17:57)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="27782"></span>
<div id="comment-27782" class="comment">
<div id="post-27782-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The homepage <a href="http://www.malldatabase.com">can be viewed here</a>.</p>
<p>But the rest of the page is displaying fine, so I don't think it's a server issue. Is there any other way that I could determine what the problem is?</p>
</div>
<div id="comment-27782-info" class="comment-info">
<span class="comment-age">(04 Nov '13, 15:28)</span> <span class="comment-user userinfo">nyancat</span>
</div>
</div>
<span id="27784"></span>
<div id="comment-27784" class="comment">
<div id="post-27784-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>At the moment I can see only empty div's where the code to show openlayers should be. So there must be something wrong with your code or with your server configuration.</p>
</div>
<div id="comment-27784-info" class="comment-info">
<span class="comment-age">(04 Nov '13, 16:07)</span> <span class="comment-user userinfo">RM87</span>
</div>
</div>
<span id="27839"></span>
<div id="comment-27839" class="comment">
<div id="post-27839-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do you generate the HTML via PHP or something?</p>
</div>
<div id="comment-27839-info" class="comment-info">
<span class="comment-age">(06 Nov '13, 08:03)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-27760" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27760-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

