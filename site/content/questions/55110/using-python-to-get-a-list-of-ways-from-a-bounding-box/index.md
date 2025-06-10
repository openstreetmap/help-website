+++
type = "question"
title = "Using python to get a list of ways from a bounding box"
description = '''Hello every one, Just recently started getting acquainted with OSM. I have used the Map function in the python module osmapi to download a bounding box. My code is as follows: from osmapi import OsmApi myApi = OsmApi()  bbox = myApi.Map(88.5052,23.4966,88.9680,23.8513)  I now want to get the list of...'''
date = "2017-03-15T16:29:00Z"
lastmod = "2017-03-17T13:40:00Z"
weight = 55110
keywords = [ "download", "ways", "osmapi_python", "bbox", "python" ]
aliases = [ "/questions/55110" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using python to get a list of ways from a bounding box](/questions/55110/using-python-to-get-a-list-of-ways-from-a-bounding-box)

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
<span id="post-55110-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55110-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55110-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello every one, Just recently started getting acquainted with OSM. I have used the Map function in the python module osmapi to download a bounding box. My code is as follows:</p>
<pre><code>from osmapi import OsmApi
myApi = OsmApi()  
bbox = myApi.Map(88.5052,23.4966,88.9680,23.8513)</code></pre>
<p>I now want to get the list of ways inside this bounding box using python code. Is this possible? If so, would any one be so kind as to give pointers on how to go about doing so?</p>
<p>Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-osmapi_python" rel="tag" title="see questions tagged &#39;osmapi_python&#39;">osmapi_python</span> <span class="post-tag tag-link-bbox" rel="tag" title="see questions tagged &#39;bbox&#39;">bbox</span> <span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Mar '17, 16:29</strong></p>
<img src="https://secure.gravatar.com/avatar/c90b2bba1514cbd750b8fadf7e90b3da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="imonike&#39;s gravatar image" />
<p><span>imonike</span><br />
<span class="score" title="96 reputation points">96</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="imonike has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Mar '17, 09:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-55110" class="comments-container">
&#10;</div>
<div id="comment-tools-55110" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55110-form-container" class="comment-form-container">
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

<span id="55111"></span>

<div id="answer-container-55111" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55111-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55111-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55111-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You shouldn't use that module if you just want to fetch data, it accesses an API intended for editing.</p>
<p>Take a look at the Overpass module for accessing data:</p>
<p><a href="https://github.com/mvexel/overpass-api-python-wrapper">https://github.com/mvexel/overpass-api-python-wrapper</a></p>
<p>Or maybe OSMAlchemy:</p>
<p><a href="https://pypi.python.org/pypi/OSMAlchemy/">https://pypi.python.org/pypi/OSMAlchemy/</a></p>
<p>I like to just write an Overpass script and embed that rather than using a wrapper.</p>
<p>If you do intend to do programmatic editing, consider modifying the data using a script and then using JOSM to interact with the API (and be aware of the policy on automatic edits: <a href="http://wiki.openstreetmap.org/wiki/Automated_edits">http://wiki.openstreetmap.org/wiki/Automated_edits</a> ).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Mar '17, 17:07</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-55111" class="comments-container">
<span id="55127"></span>
<div id="comment-55127" class="comment">
<div id="post-55127-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks so much maxerickson. I have come across the Overpass API, I guess it is time to dig in!! OSMAlchemy looks interesting. I still have a question, please don't be offended, it is really getting at my curiosity. Now the Map function I mentioned returns a list of dict objects that representing the nodes in the bounding longitudes and latitudes specified. If ways are a collection of nodes, isn't possible to get the list of ways I am looking for from the data I downloaded with the Map function?</p>
<p>Thank you for your patience.</p>
</div>
<div id="comment-55127-info" class="comment-info">
<span class="comment-age">(16 Mar '17, 14:53)</span> <span class="comment-user userinfo">imonike</span>
</div>
</div>
<span id="55128"></span>
<div id="comment-55128" class="comment">
<div id="post-55128-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't know the module. According to <a href="http://osmapi.metaodi.ch/#osmapi.OsmApi.OsmApi.Map">http://osmapi.metaodi.ch/#osmapi.OsmApi.OsmApi.Map</a> the ways should be in the same dict.</p>
</div>
<div id="comment-55128-info" class="comment-info">
<span class="comment-age">(16 Mar '17, 17:41)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="55157"></span>
<div id="comment-55157" class="comment">
<div id="post-55157-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks maxerickson. I really appreciate. I have visited that page. It's where I learnt about the Map function. Here is a fragment of the data returned:[{u'data': {u'changeset': 45126331, u'uid': 4384747, u'timestamp': datetime.datetime(2017, 1, 13, 7, 55, 35), u'lon': 88.5834267, u'visible': True, u'version': 3, u'user': u'\u30aa\u30c1\u30a2\u30a4\u30b3\u30e9\u30dc', u'lat': 23.806732, u'tag': {u'source': u'AND'}, u'id': 245716849}, u'type': u'node'},--I guess that would represent a single node. There are similar nodes in dict form making up a list. There doesn't seem to be anything to let u know which nodes make up a way. Tried using the NodeWays method but my conn was forcibly closed by the host. Guess my code was violating their download rules. Anyway started looking at the Overpass API. Many thanks for the help. Cheers</p>
</div>
<div id="comment-55157-info" class="comment-info">
<span class="comment-age">(17 Mar '17, 13:40)</span> <span class="comment-user userinfo">imonike</span>
</div>
</div>
</div>
<div id="comment-tools-55111" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55111-form-container" class="comment-form-container">
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

