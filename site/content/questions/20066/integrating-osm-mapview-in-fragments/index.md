+++
type = "question"
title = "Integrating OSM MapView in fragments"
description = '''As per asked in here... I am trying to implement OSM MapView in fragments. I&#x27;ve seen people done this in onCreateView return new MapView(getActivity(), 256);  However I am not sure how to change my implementation of an Activity into Fragments... right now my Activity codes are like this: MapView myO...'''
date = "2013-02-20T14:56:00Z"
lastmod = "2013-02-21T08:27:00Z"
weight = 20066
keywords = [ "mapview", "osmdroid", "fragments" ]
aliases = [ "/questions/20066" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Integrating OSM MapView in fragments](/questions/20066/integrating-osm-mapview-in-fragments)

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
<span id="post-20066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20066-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>As per asked in <a href="http://stackoverflow.com/questions/14897143/integrating-osmdroid-with-fragments">here</a>... I am trying to implement OSM MapView in fragments. I've seen people done this in onCreateView</p>
<pre><code>return new MapView(getActivity(), 256);</code></pre>
<p>However I am not sure how to change my implementation of an Activity into Fragments... right now my Activity codes are like this:</p>
<pre><code>MapView myOpenMapView;
&#10;public void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
&#10;    mResourceProxy = new DefaultResourceProxyImpl(getApplicationContext());
    setContentView(R.layout.offline_map_activity);
    myOpenMapView = (MapView) findViewById(R.id.openmapview);
    myOpenMapView.getTileProvider().clearTileCache();
&#10;    //.... code continues
}</code></pre>
<p>But I'm not sure how to convert this part of the code when implemented in Fragments:</p>
<pre><code>setContentView(R.layout.offline_map_activity);
myOpenMapView = (MapView) findViewById(R.id.openmapview);</code></pre>
<p>How do I instantiate the MapView object properly and return it in the onCreateView method?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapview" rel="tag" title="see questions tagged &#39;mapview&#39;">mapview</span> <span class="post-tag tag-link-osmdroid" rel="tag" title="see questions tagged &#39;osmdroid&#39;">osmdroid</span> <span class="post-tag tag-link-fragments" rel="tag" title="see questions tagged &#39;fragments&#39;">fragments</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Feb '13, 14:56</strong></p>
<img src="https://secure.gravatar.com/avatar/8e2f3652fadd1fc58cbd9780977ab5d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lyk&#39;s gravatar image" />
<p><span>lyk</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lyk has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Feb '13, 00:25</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-20066" class="comments-container">
<span id="20080"></span>
<div id="comment-20080" class="comment">
<div id="post-20080-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hmm, this site is not really about coding with some specific toolkit... However, please link your post here also in stackoverflow to mitigate the bad effects of crossposting.</p>
</div>
<div id="comment-20080-info" class="comment-info">
<span class="comment-age">(21 Feb '13, 00:31)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="20081"></span>
<div id="comment-20081" class="comment">
<div id="post-20081-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I already hyperlinked the stackoverflow question under the word "here". Oh, is this forum not about openstreetmap/OSMDroid? If that's the case where can I ask about implementing fragments with OSMDroid?</p>
</div>
<div id="comment-20081-info" class="comment-info">
<span class="comment-age">(21 Feb '13, 03:31)</span> <span class="comment-user userinfo">lyk</span>
</div>
</div>
<span id="20088"></span>
<div id="comment-20088" class="comment">
<div id="post-20088-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@lyk</span>: I saw the "here". I mean that it would be good to insert a link into your question at stackoverflow.</p>
<p>A <a href="http://forum.openstreetmap.org/">forum</a> or a <span>mailing list</span> (e.g. dev?) are probably better suited - but you may get an answer here, too. Wait a day or two.</p>
</div>
<div id="comment-20088-info" class="comment-info">
<span class="comment-age">(21 Feb '13, 08:27)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-20066" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20066-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

