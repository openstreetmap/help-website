+++
type = "question"
title = "Embedded HTML displays zoomed out"
description = '''I just embedded the HTML provided by the Export function into a web page, and when it displays on my site, the map is zoomed out to the max: it shows the whole world instead of the area I selected. How can I make it display like it used to a week or so ago, zoomed exactly to the area I selected, jus...'''
date = "2013-02-27T10:17:00Z"
lastmod = "2023-01-16T13:11:00Z"
weight = 20335
keywords = [ "osm.org", "html", "export", "zoom", "embedded" ]
aliases = [ "/questions/20335" ]
osqa_answers = 8
osqa_accepted = false
+++

<div class="headNormal">

# [Embedded HTML displays zoomed out](/questions/20335/embedded-html-displays-zoomed-out)

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
<span id="post-20335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20335-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-20335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I just embedded the HTML provided by the Export function into a web page, and when it displays on my site, the map is zoomed out to the max: it shows the whole world instead of the area I selected.</p>
<p>How can I make it display like it used to a week or so ago, zoomed exactly to the area I selected, just as it was when I exported it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm.org" rel="tag" title="see questions tagged &#39;osm.org&#39;">osm.org</span> <span class="post-tag tag-link-html" rel="tag" title="see questions tagged &#39;html&#39;">html</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span> <span class="post-tag tag-link-embedded" rel="tag" title="see questions tagged &#39;embedded&#39;">embedded</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Feb '13, 10:17</strong></p>
<img src="https://secure.gravatar.com/avatar/4cd050b9e2734e903149e94ed29c5104?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frisket&#39;s gravatar image" />
<p><span>frisket</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frisket has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Feb '13, 21:57</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-20335" class="comments-container">
&#10;</div>
<div id="comment-tools-20335" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20335-form-container" class="comment-form-container">
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

8 Answers:

</div>

</div>

<span id="30839"></span>

<div id="answer-container-30839" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30839-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30839-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-30839-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should find that you can adjust your view of the map on the OpenStreetMap website, to make adjustments to the resulting generated HTML (fiddle with your view, e.g. to zoom in/out a bit, and then re-do the copy and paste of the HTML into your website)</p>
<p>But you may well find the zoom you see on the website (in a wide window) is higher than the zoom level in the resulting embedded map (narrow iframe), so if you specifically want a higher zoom level, simply zoom in a bit more to compensate.</p>
<p>What you actually need to pay attention to, is what extents of the map can you see on screen, to the left and right and sides. These will still be visible within the narrower embedded view. <strong>It's designed to preserve the extents of what you can see, rather than preserve the centre and zoom level of what you can see</strong>.</p>
<p>If you <em>are</em> interested in parameters, you can see that generated HTML is an iframe with a 'src' parameter. This points to embed.html with the parameter 'bbox'. It is this parameter which represents the bounding box coordinates of this extent of what's visible on the screen. This is telling it indirectly what the zoom level will be.</p>
<p>Another interesting consequence of this approach is that you would get a higher zoom level if you made your iframe bigger (change the width and height parameters in the generated HTML)</p>
<p>But as for specifying a zoom level parameter more directly in the URL, that is currently not supported. The <a href="https://github.com/openstreetmap/openstreetmap-website/blob/3bee80e0dce15654f36bcf253f58a6b098e4baa4/app/assets/javascripts/embed.js.erb%0A">embed.html javascript</a> is relatively simple, and only supports the bbox parameter as generated by the share feature.</p>
<p>We <em>could</em> enhance this to add more options, but the central OpenStreetMap website isn't really about hosting iframe contents for people, and if you have more sophisticated requirements as a web developer, you should do one of the following (in increasing order of complexity)</p>
<ul>
<li>Use <a href="http://wiki.openstreetmap.org/wiki/UMap">umap</a>, to create a iframe embeddable map with all sorts of options. umap would be hosting the contents of your iframe.</li>
<li>Use <a href="http://wiki.openstreetmap.org/wiki/Static_map_images">Static map images</a> to generate a static image URL with all sorts of options. Your chosen service would be hosting the static image (Note: Although static images might seem rather basic, they're also lean and elegant, and can be linkified to somewhere like the OpenStreetMap homepage to offer a more dynamic view)</li>
<li><a href="http://wiki.openstreetmap.org/wiki/Deploying_your_own_Slippy_Map">Deploying your own slippy map</a>. Use leafletJS or OpenLayers to host the javascript yourself with full control over, zoom and markers etc.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '14, 14:29</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Feb '14, 16:19</strong> </span></p>
</div>
</div>
<div id="comments-container-30839" class="comments-container">
&#10;</div>
<div id="comment-tools-30839" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30839-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20347"></span>

<div id="answer-container-20347" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20347-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20347-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-20347-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>So I assume that you used the <a href="http://wiki.openstreetmap.org/wiki/Export">Export</a> tab of openstreetmap.org site.</p>
<p>There it is documented that the exported HTML code is displaying the <em>current</em> map view ... so if this does not work for you, it may be a software bug at osm.org</p>
<p>Please try again, or show us the delivered HTML code you have embedded to your website via <a href="http://en.wikipedia.org/wiki/Pastebin">Pastebin</a> or some similar service if it is too much text.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Feb '13, 18:56</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-20347" class="comments-container">
<span id="20376"></span>
<div id="comment-20376" class="comment">
<div id="post-20376-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Here is the code I pasted:</p>
<p>iframe src="http://www.openstreetmap.org/export/embed.html?bbox=-8.4973,51.89139,-8.48863,51.89476&amp;layer=mapnik&amp;marker=51.89297,-8.49417" width="425" height="350"&gt;&lt;/iframe&gt;<br />
<span class="small"><a href="http://www.openstreetmap.org/?lat=51.893074999999996&amp;lon=-8.492965&amp;zoom=16&amp;layers=M&amp;mlat=51.89297&amp;mlon=-8.49417">View Larger Map</a></span></p>
<p>This is showing at <a href="http://www.ucc.ie/en/support/it/offices/">http://www.ucc.ie/en/support/it/offices/</a> (click on the blue bar to reveal). There is a screenshot of what I see in FF or Chrome here: <a href="http://www.ucc.ie/zoomed-out-map.png">http://www.ucc.ie/zoomed-out-map.png</a></p>
</div>
<div id="comment-20376-info" class="comment-info">
<span class="comment-age">(28 Feb '13, 11:21)</span> <span class="comment-user userinfo">frisket</span>
</div>
</div>
<span id="20405"></span>
<div id="comment-20405" class="comment">
<div id="post-20405-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>the live example works as expected for me (Firefox) - at least now.</p>
</div>
<div id="comment-20405-info" class="comment-info">
<span class="comment-age">(28 Feb '13, 21:56)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-20347" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20347-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20362"></span>

<div id="answer-container-20362" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20362-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20362-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-20362-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>the generated HTML code by the export panel on <a href="http://www.openstreetmap.org/">http://www.openstreetmap.org/</a> (I guess you mean that) includes a parameter "bbox" which defines the area which should be shown. I just tried an example export and the HTML code did not show the whole world but a much smaller area which I had in my current osm.org view.</p>
<p>Go to <a href="http://www.openstreetmap.org/?lat=50.1331&amp;lon=8.6917&amp;zoom=12&amp;layers=M">http://www.openstreetmap.org/?lat=50.1331&amp;lon=8.6917&amp;zoom=12&amp;layers=M</a> select export, select the HTML option. There you are:</p>
<p>&lt;iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://www.openstreetmap.org/export/embed.html?bbox=8.5628,50.0781,8.8217,50.1877&amp;amp;layer=mapnik" style="border: 1px solid black"&gt;&lt;/iframe&gt;</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Feb '13, 22:27</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Feb '13, 22:36</strong> </span></p>
</div>
</div>
<div id="comments-container-20362" class="comments-container">
<span id="20377"></span>
<div id="comment-20377" class="comment">
<div id="post-20377-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>OK, thanks. Yes, that's exactly what I did. Some experimenting shows that this works fine in a plain hand-made HTML5 doc, so the problem is a conflict with our site style (CSS/JS): it works when I place it outside the unfolding menubar.</p>
<p>Strange that it worked fine last week...someone must have changed the CSS or JS in the meantime.</p>
<p>Thanks for the help.</p>
</div>
<div id="comment-20377-info" class="comment-info">
<span class="comment-age">(28 Feb '13, 11:27)</span> <span class="comment-user userinfo">frisket</span>
</div>
</div>
<span id="20378"></span>
<div id="comment-20378" class="comment">
<div id="post-20378-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>BTW how do I mark this as Closed?</p>
</div>
<div id="comment-20378-info" class="comment-info">
<span class="comment-age">(28 Feb '13, 11:27)</span> <span class="comment-user userinfo">frisket</span>
</div>
</div>
<span id="20379"></span>
<div id="comment-20379" class="comment">
<div id="post-20379-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There's a tick / checkmark that you can select under the correct answer. Do that, and it'll appear as "answered".</p>
<p>(and no, it's not particularly obvious!).</p>
</div>
<div id="comment-20379-info" class="comment-info">
<span class="comment-age">(28 Feb '13, 11:32)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="20404"></span>
<div id="comment-20404" class="comment">
<div id="post-20404-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@frisket</span>: thank you for your feedback, that's helpful for all others.</p>
</div>
<div id="comment-20404-info" class="comment-info">
<span class="comment-age">(28 Feb '13, 21:49)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-20362" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20362-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86105"></span>

<div id="answer-container-86105" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86105-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86105-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86105-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Since this problem still persists (both in Firefox and Chrome), no one has posted a solution that actually works and reloading always helps, I offer the following workaround.</p>
<p>The embed iframe:</p>
<pre><code>&lt;iframe id=&quot;map&quot; {rest_of_OpenStreetMap_embed_code} &gt;&lt;/iframe&gt;</code></pre>
<p>The script:</p>
<pre><code>&lt;script type=&quot;text/javascript&quot; defer&gt;
function reload(id) 
{
    var buggyid = document.getElementById(id);
    buggyid.src = buggyid.src;
}
&#10;setTimeout(reload, 500, &#39;map&#39;);
&lt;/script&gt;</code></pre>
<p>This reloads the iframe with id="map" 500ms after everything has loaded. 500ms is enough in my experience. Try to increase the value if it still doesn't load correctly. Also, you can put a button or image link over or near the iframe to call the script reload('map') manually so the visitor knows what to do in case the bug should still occur or return.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Nov '22, 20:11</strong></p>
<img src="https://secure.gravatar.com/avatar/3fc9d15f7807c449a736c89ec931b9cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="unicomplex&#39;s gravatar image" />
<p><span>unicomplex</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="unicomplex has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Nov '22, 20:14</strong> </span></p>
</div>
</div>
<div id="comments-container-86105" class="comments-container">
<span id="86106"></span>
<div id="comment-86106" class="comment">
<div id="post-86106-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The only thing I haven't tried yet (actually, not figured out yet) is to defer the iframe loading so the wrong version isn't loaded in the first place but only after 500ms.</p>
</div>
<div id="comment-86106-info" class="comment-info">
<span class="comment-age">(07 Nov '22, 20:17)</span> <span class="comment-user userinfo">unicomplex</span>
</div>
</div>
<span id="86521"></span>
<div id="comment-86521" class="comment">
<div id="post-86521-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Had this exact problem and this solution worked. Thanks for posting.</p>
</div>
<div id="comment-86521-info" class="comment-info">
<span class="comment-age">(16 Jan '23, 13:11)</span> <span class="comment-user userinfo">Togethernet</span>
</div>
</div>
</div>
<div id="comment-tools-86105" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86105-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="51323"></span>

<div id="answer-container-51323" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51323-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hey, it's my first post here :) It's not ideal way, but here's rewritten method from my PHP's class to use as separate function. It makes iframe URL from input data: lat, lon and area.</p>
<p>The function you'd use is <code>getBBox</code> function to get array. <code>$lat</code> and <code>$lon</code> is latitude and longitude in decimal form (i.e. 54.3242342). <code>$area</code> is how much area do you want to see in meters (if you want to have map starting 500 meters above and ending 500 meters below, use 1000).</p>
<p>It could be written better, but you have an idea. <code>getCoordOffset</code> is internal function, so I'm not explaining it, unless anybody wants it. For easiness of use, <strong>I release it as public domain, wherever it's possible and CC-0 for other cases</strong> - if you actually want to use attribution, just use my nick or change it to website name coming from it.</p>
<p>The algorithm is not ideal, but it should be ok for this use. If you don't want marker, remove everything after <code>layer=mapnik</code> from sprintf template URL and remove 4 and 5 index from getBBox function array.</p>
<p>As the result of the function is an array, you can feed it to <code>vsprintf()</code> - array version of <code>sprintf()</code>. In the example you have ready to use vsprintf function. If you are going to debug it by pasting URL in browser, you won't see marker, <strong>unless you replace <code>&amp;amp;</code> in URL with <code>&amp;</code></strong>.</p>
<pre><code>function getCoordOffset($what, $lat, $lon, $offset) {
    $earthRadius = 6378137;
    $coord = [0 =&gt; $lat, 1 =&gt; $lon];
&#10;    $radOff = $what === 0 ? $offset / $earthRadius : $offset / ($earthRadius * cos(M_PI * $coord[0] / 180));
    return $coord[$what] + $radOff * 180 / M_PI;    
}
&#10;function getBBox($lat, $lon, $area) {
$offset = $area / 2;
return [
    0 =&gt; getCoordOffset(1, $lat, $lon, -$offset),
    1 =&gt; getCoordOffset(0, $lat, $lon, -$offset),
    2 =&gt; getCoordOffset(1, $lat, $lon, $offset),
    3 =&gt; getCoordOffset(0, $lat, $lon, $offset),
    4 =&gt; $lat,
    5 =&gt; $lon
]; // 0 = minlon, 1 = minlat, 2 = maxlon, 3 = maxlat, 4,5 = original val (marker)
}</code></pre>
<p>If you want bounding box for area 1x1km, now you need to count it like that:</p>
<pre><code>$bbox = getBBox(52.13543, 19.43434, 1000);
$url = vsprintf(&#39;http://www.openstreetmap.org/export/embed.html?bbox=%.15f%%2C%.15f%%2C%.15f%%2C%.15f&amp;amp;layer=mapnik&amp;amp;marker=%.15f%%2C%.15f&#39;, $bbox); // merge result array with template string - URL for iframe</code></pre>
<p>By the way I had problems with map totally zoomed out, but it's rather OSM bug. I changed offset to smaller, then I got back to earlier offset and it worked. Maybe malformed cookies or so. It happened once.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Aug '16, 01:58</strong></p>
<img src="https://secure.gravatar.com/avatar/822ec1ec8c52099b8a3cca7c85cddf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KrzysiuNet&#39;s gravatar image" />
<p><span>KrzysiuNet</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KrzysiuNet has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51323" class="comments-container">
&#10;</div>
<div id="comment-tools-51323" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51323-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73902"></span>

<div id="answer-container-73902" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73902-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73902-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73902-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm having a similar problem. The embedded iframe works fine for a while, then after one or two browser refreshes the view I wanted is replaced by a map of the world.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Apr '20, 08:49</strong></p>
<img src="https://secure.gravatar.com/avatar/6824a192111b6575ff403b7f328c1ef9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VirtualMountains&#39;s gravatar image" />
<p><span>VirtualMount...</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VirtualMountains has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73902" class="comments-container">
<span id="78420"></span>
<div id="comment-78420" class="comment">
<div id="post-78420-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, i have the same problem...</p>
</div>
<div id="comment-78420-info" class="comment-info">
<span class="comment-age">(19 Jan '21, 19:22)</span> <span class="comment-user userinfo">manu4564618</span>
</div>
</div>
</div>
<div id="comment-tools-73902" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73902-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78419"></span>

<div id="answer-container-78419" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78419-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78419-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78419-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hey, i have the same problem!</p>
<p>Is there anybody who can help?</p>
<p>Greetings!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jan '21, 19:22</strong></p>
<img src="https://secure.gravatar.com/avatar/5ce56df63bdd10c3c5078f358a69f7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manu4564618&#39;s gravatar image" />
<p><span>manu4564618</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manu4564618 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78419" class="comments-container">
&#10;</div>
<div id="comment-tools-78419" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78419-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78642"></span>

<div id="answer-container-78642" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78642-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78642-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78642-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>While exporting check if in the url you got '%2C' or just '%'. In first case, try to remove all '2C' that appears in the url after '%' or replace by comma ','. Strange enough, it is sometimes working, but not always.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Feb '21, 14:59</strong></p>
<img src="https://secure.gravatar.com/avatar/7b2d774e27692ea45a7650138c057c03?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ststag&#39;s gravatar image" />
<p><span>ststag</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ststag has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Feb '21, 15:51</strong> </span></p>
</div>
</div>
<div id="comments-container-78642" class="comments-container">
<span id="78788"></span>
<div id="comment-78788" class="comment">
<div id="post-78788-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! but for me this is not working, unfortunately. The box is white now...</p>
</div>
<div id="comment-78788-info" class="comment-info">
<span class="comment-age">(10 Feb '21, 15:48)</span> <span class="comment-user userinfo">manu4564618</span>
</div>
</div>
</div>
<div id="comment-tools-78642" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78642-form-container" class="comment-form-container">
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

