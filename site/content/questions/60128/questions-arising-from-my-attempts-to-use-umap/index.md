+++
type = "question"
title = "Questions arising from my attempts to use uMap"
description = '''uMap appears to offer a solution: I wish to display different types of barrier, e.g. kissing gate, gate, stile, etc., over selected and different types of Public Rights of Way (PRoW). Three questions arise:   What is the purpose of logging in or signing in, and what is the meaning of &quot;Please choose ...'''
date = "2017-10-15T09:32:00Z"
lastmod = "2017-10-22T16:15:00Z"
weight = 60128
keywords = [ "umap", "save" ]
aliases = [ "/questions/60128" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Questions arising from my attempts to use uMap](/questions/60128/questions-arising-from-my-attempts-to-use-umap)

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
<span id="post-60128-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60128-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60128-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>uMap appears to offer a solution: I wish to display different types of barrier, e.g. kissing gate, gate, stile, etc., over selected and different types of Public Rights of Way (PRoW). Three questions arise:</p>
<ol>
<li><p>What is the purpose of logging in or signing in, and what is the meaning of "Please choose a provider"? My instinct is to select OSM, but what does it achieve?</p></li>
<li><p>I have created ways representing PRoWs and nodes representing barriers in Overpass Turbo and exported them as .kml files. I can import them and adjust their styles. I click 'Save' that gives me a file "untitled_map.umap". I do not know how to open that file to carry out further work, say.</p></li>
<li><p>The range of symbols available appears to be limited. Is there a facility to use third-party symbols or one's own creations? If so, in what format?</p></li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span> <span class="post-tag tag-link-save" rel="tag" title="see questions tagged &#39;save&#39;">save</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Oct '17, 09:32</strong></p>
<img src="https://secure.gravatar.com/avatar/ffcc41f13929627742b4936ec178c6f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="silver%20mapper&#39;s gravatar image" />
<p><span>silver mapper</span><br />
<span class="score" title="256 reputation points">256</span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="27 badges"><span class="silver">●</span><span class="badgecount">27</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="silver mapper has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Oct '17, 10:28</strong> </span></p>
</div>
</div>
<div id="comments-container-60128" class="comments-container">
&#10;</div>
<div id="comment-tools-60128" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60128-form-container" class="comment-form-container">
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

<span id="60129"></span>

<div id="answer-container-60129" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60129-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60129-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60129-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>All maps that you create are attached to an account. So they are "your" maps and can be listed when you login. Without login, umap does not know who created the map. In that case you have to remember the links to all maps that you created.</p>
<p>There is no need to export the barriers from Overpass and import them later on. You can use Overpass directly from within umap, see <a href="http://www.mappa-mercia.org/2014/09/creating-an-always-up-to-date-map.html">Mappa Mercia's blog</a> on how to achieve that.</p>
<p>Under shape properties, you can set the icon. On one hand there is the list that you probably saw, but you can also set your own URL to a gif/png/jpg. e.g. <a href="https://raw.githubusercontent.com/username/umapicons/master/%7Bspecies%7D.jpg">https://raw.githubusercontent.com/username/umapicons/master/{species}.jpg</a> By using braces, you can refer to data fields in your data. In this example, the species tag value will become the name of the file.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Oct '17, 09:52</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-60129" class="comments-container">
<span id="60130"></span>
<div id="comment-60130" class="comment">
<div id="post-60130-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>escada</p>
<p>I thank you for your immediate and constructive reply. I lack knowledge of how to create or use URLs in such contexts as this and am unsure what your final two sentences mean but will try to put into practice your comments.</p>
</div>
<div id="comment-60130-info" class="comment-info">
<span class="comment-age">(15 Oct '17, 10:27)</span> <span class="comment-user userinfo">silver mapper</span>
</div>
</div>
<span id="60143"></span>
<div id="comment-60143" class="comment">
<div id="post-60143-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You will have data with tags such as barrier=stile and barrier=kissing_gate You probably want to have different icons for the two. So you will have e.g. a file stile.jpg and kissing_gate.jpg You place those two files on a website. They will then be accessible via <a href="http://host/path/stile.jpg">http://host/path/stile.jpg</a> and <a href="http://host/path/kissing_gate.jpg">http://host/path/kissing_gate.jpg</a> <em>host</em> and <em>path</em> depend on the service you are using. Now you can use <a href="http://host/path/%7Bbarrier%7D.jpg">http://host/path/{barrier}.jpg</a> in your umap (replace host and path with your service). Whenever umap finds a stile-barrier in your data it will display the stile.jpg icon. umap will replace {barrier} with stile if that is the value of the barrier you want to display. This works fine with the Overpass technique explained in Mappa Mercia's blog. Don't know for other data formats you can use with umap. Hope this clarifies the last 2 sentences a bit</p>
</div>
<div id="comment-60143-info" class="comment-info">
<span class="comment-age">(16 Oct '17, 04:46)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="60147"></span>
<div id="comment-60147" class="comment">
<div id="post-60147-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>escada</p>
<p>I appreciate very much your persistence in trying to help me; you understand perfectly what I seek to do.</p>
<p>I failed with Mappa Mercia's blog instructions. I have obtained a parish boundary, its footpaths, bridleways, restricted byways, gates, kissing gates and stiles in Overpass Turbo, and copied/imported all as individual layers into uMap. I have coloured the lines and pins appropriately on a monochrome map background, which works well.</p>
<p>I possess .jpg images for each barrier type that I created for use in my Locus Map app. I regret I am wholly ignorant in knowing how to get them onto a website.</p>
<p>Must the images be a particular size?</p>
</div>
<div id="comment-60147-info" class="comment-info">
<span class="comment-age">(16 Oct '17, 07:39)</span> <span class="comment-user userinfo">silver mapper</span>
</div>
</div>
<span id="60151"></span>
<div id="comment-60151" class="comment">
<div id="post-60151-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I don't know whether the images should have a particular size. Don't you have access to a website where you share e.g. your photos such as Flickr, or one of the many others? The drawback is that you cannot always choose the name of your file. This is possible on e.g. the github website I was mentioning.</p>
</div>
<div id="comment-60151-info" class="comment-info">
<span class="comment-age">(16 Oct '17, 10:27)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-60129" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60129-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60218"></span>

<div id="answer-container-60218" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60218-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60218-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60218-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I resorted to two generations down the line: my grandson placed .png images of gates, kissing gates and stiles onto a website and sent me links. I pasted the .urls into uMap successfully and am pleased with the result. In answer to "Must the images be a particular size?", they are sized to fit the standard icons available, it seems.<br />
I think "Default" and "Drop" are the only ones to which symbols can apply. "Default" worked perfectly for the shape of my image. I wish I could attach a file.</p>
<p>I have learnt so much about uMap in less than a week. I am very impressed with what I have been able to achieve. I consider my three questions asked originally to be satisfied completely and with many thanks to escada.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Oct '17, 16:15</strong></p>
<img src="https://secure.gravatar.com/avatar/ffcc41f13929627742b4936ec178c6f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="silver%20mapper&#39;s gravatar image" />
<p><span>silver mapper</span><br />
<span class="score" title="256 reputation points">256</span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="27 badges"><span class="silver">●</span><span class="badgecount">27</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="silver mapper has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-60218" class="comments-container">
&#10;</div>
<div id="comment-tools-60218" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60218-form-container" class="comment-form-container">
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

