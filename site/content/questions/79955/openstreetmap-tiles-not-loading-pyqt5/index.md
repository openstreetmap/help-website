+++
type = "question"
title = "OpenStreetMap Tiles Not Loading PYQt5"
description = '''Good day I had used folium map to load in an OpenStreetMap for my project. It had worked for a few months then when I tried opening the programme again it does not display OpenStreetMap tiles. However saving the folium map as HTML file and opening that file it would display. So I am wondering what i...'''
date = "2021-04-30T13:59:00Z"
lastmod = "2021-04-30T19:07:00Z"
weight = 79955
keywords = [ "python", "tiles", "folium", "pyqt5" ]
aliases = [ "/questions/79955" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [OpenStreetMap Tiles Not Loading PYQt5](/questions/79955/openstreetmap-tiles-not-loading-pyqt5)

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
<span id="post-79955-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79955-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79955-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Good day I had used folium map to load in an OpenStreetMap for my project. It had worked for a few months then when I tried opening the programme again it does not display OpenStreetMap tiles. However saving the folium map as HTML file and opening that file it would display. So I am wondering what is wrong. Did the way how things displayed in PyQt5 changed? Please help.</p>
<p>See below for relevant code:</p>
<p>app = QtWidgets.QApplication(sys.argv)</p>
<p>mapCanvas = QtWebEngineWidgets.QWebEngineView() loc = {'Georgetown':[6.804258931351689, -58.148124600778885]} Gmap = folium.Map(location=loc['Georgetown'],zoom_start=14, tiles='OpenStreetMap') data = io.BytesIO() Gmap.save(data, close_file=False) mapCanvas.setHtml(self.data.getvalue().decode()) mapCanvas.show()</p>
<p>sys.exit(app.exec_())</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-folium" rel="tag" title="see questions tagged &#39;folium&#39;">folium</span> <span class="post-tag tag-link-pyqt5" rel="tag" title="see questions tagged &#39;pyqt5&#39;">pyqt5</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Apr '21, 13:59</strong></p>
<img src="https://secure.gravatar.com/avatar/8f8432b328ec47d74cff6f329d6fbbdd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nicolas%20Stephney&#39;s gravatar image" />
<p><span>Nicolas Step...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nicolas Stephney has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79955" class="comments-container">
<span id="79956"></span>
<div id="comment-79956" class="comment">
<div id="post-79956-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Without some sort of error it'll be difficult for anyone to comment. all you've said so far is that "something that no-one else has access to used to work and now does not". Have you tried asking the people who are responsible for the "QtWebEngineWidgets.QWebEngineView()" that you mention?</p>
</div>
<div id="comment-79956-info" class="comment-info">
<span class="comment-age">(30 Apr '21, 16:18)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="79957"></span>
<div id="comment-79957" class="comment">
<div id="post-79957-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I will contact those responsible for QWebEngineView(). No error was raised in the program it just appeared grey with the markers I had placed on the map showing and the zoom in and out controls. I had seen on reddit a similar problem occurred with unloaded tiles. <a href="https://www.reddit.com/r/openstreetmap/comments/mh0ixw/tiles_not_loading/">https://www.reddit.com/r/openstreetmap/comments/mh0ixw/tiles_not_loading/</a></p>
</div>
<div id="comment-79957-info" class="comment-info">
<span class="comment-age">(30 Apr '21, 16:36)</span> <span class="comment-user userinfo">Nicolas Step...</span>
</div>
</div>
<span id="79958"></span>
<div id="comment-79958" class="comment">
<div id="post-79958-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was thinking that openstreetmap would have known the API call and if it had changed to know whether something needed to be added to reveal the map.</p>
</div>
<div id="comment-79958-info" class="comment-info">
<span class="comment-age">(30 Apr '21, 17:04)</span> <span class="comment-user userinfo">Nicolas Step...</span>
</div>
</div>
<span id="79959"></span>
<div id="comment-79959" class="comment">
<div id="post-79959-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I decided to change the tiles to "Stamen Terrain" instead of OpenStreetMap and it displayed the map. So definitely the problem is with OpenStreetMap call that makes those tiles not load. So I do not know what may have caused the issue of OSM tiles not being loaded.</p>
</div>
<div id="comment-79959-info" class="comment-info">
<span class="comment-age">(30 Apr '21, 18:20)</span> <span class="comment-user userinfo">Nicolas Step...</span>
</div>
</div>
<span id="79960"></span>
<div id="comment-79960" class="comment">
<div id="post-79960-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Any consumer of OSM tiles needs to follow <a href="https://operations.osmfoundation.org/policies/tiles/">https://operations.osmfoundation.org/policies/tiles/</a> . If yours does not, it may be blocked.</p>
</div>
<div id="comment-79960-info" class="comment-info">
<span class="comment-age">(30 Apr '21, 19:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="79961"></span>
<div id="comment-79961" class="comment not_top_scorer">
<div id="post-79961-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh thank you so much. I was probably blocked.</p>
</div>
<div id="comment-79961-info" class="comment-info">
<span class="comment-age">(30 Apr '21, 19:07)</span> <span class="comment-user userinfo">Nicolas Step...</span>
</div>
</div>
</div>
<div id="comment-tools-79955" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-79955-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

