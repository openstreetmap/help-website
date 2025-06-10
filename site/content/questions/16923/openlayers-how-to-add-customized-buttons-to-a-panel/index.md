+++
type = "question"
title = "Openlayers: How to add customized buttons to a panel?"
description = '''Hi there i have following code : vlayer = new OpenLayers.Layer.Vector(&quot;Overlay&quot;); map.addLayer(vlayer); var panel = new OpenLayers.Control.Panel({  createControlMarkup: function (control) {  var button = document.createElement(&#x27;button&#x27;),  iconSpan = document.createElement(&#x27;span&#x27;),  textSpan = docume...'''
date = "2012-10-16T15:08:00Z"
lastmod = "2012-10-16T15:37:00Z"
weight = 16923
keywords = [ "openlayers" ]
aliases = [ "/questions/16923" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Openlayers: How to add customized buttons to a panel?](/questions/16923/openlayers-how-to-add-customized-buttons-to-a-panel)

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
<span id="post-16923-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16923-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16923-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there i have following code :</p>
<pre><code>vlayer = new OpenLayers.Layer.Vector(&quot;Overlay&quot;);
map.addLayer(vlayer);
var panel = new OpenLayers.Control.Panel({
    createControlMarkup: function (control) {
        var button = document.createElement(&#39;button&#39;),
            iconSpan = document.createElement(&#39;span&#39;),
            textSpan = document.createElement(&#39;span&#39;);
        button.setAttribute(&quot;class&quot;, &quot;controlButtons&quot;);
        iconSpan.innerHTML = &#39;&amp;nbsp;&#39;;
        button.appendChild(iconSpan);
        if (control.text) {
            textSpan.innerHTML = control.text;
        }
        button.appendChild(textSpan);
        return button;
    }
});</code></pre>
<p>and i am trying call a seperate functions on clicking the button...</p>
<pre><code>panel.addControls([
     button1 = new OpenLayers.Control.SelectFeature(vlayer, {
     title: &#39;Add the company&#39;,
     text: &#39;Add&#39;,
     onClick: addCom,
     }),
     button2 = new OpenLayers.Control.SelectFeature(vlayer, {
         title: &quot;Edit the company&quot;,
         text: &quot;Edit&quot;,
         onClick: editComp,
     }),
     button2 = new OpenLayers.Control.SelectFeature(vlayer, {
         title: &quot;Delete the company&quot;,
         text: &quot;Delete&quot;,
         onClick: delComp,
     })]);
&#10;     map.addControl(panel);</code></pre>
<p>the buttons are displaying but for some reason they are responding to click.....Please help me to sole this ...Thank YOu</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Oct '12, 15:08</strong></p>
<img src="https://secure.gravatar.com/avatar/226e87e44cb94204c59189d49e817e64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dominc&#39;s gravatar image" />
<p><span>Dominc</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dominc has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Oct '12, 15:25</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-16923" class="comments-container">
<span id="16925"></span>
<div id="comment-16925" class="comment">
<div id="post-16925-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you look through the <a href="https://help.openstreetmap.org/search/?q=openlayers&amp;Submit=Search&amp;t=question">previous openlayers questions</a> asked here, you'll see links to more relevant help sites. Openlayers isn't actually part of OSM, so it isn't really on-topic for this help site.</p>
<p>There are a bunch of OpenLayers mailing lists described <a href="http://trac.osgeo.org/openlayers/wiki/MailingLists">here</a>, and other useful resources, including an IRC channel, <a href="http://trac.osgeo.org/openlayers/">here</a>.</p>
</div>
<div id="comment-16925-info" class="comment-info">
<span class="comment-age">(16 Oct '12, 15:29)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="16927"></span>
<div id="comment-16927" class="comment">
<div id="post-16927-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks ......</p>
</div>
<div id="comment-16927-info" class="comment-info">
<span class="comment-age">(16 Oct '12, 15:37)</span> <span class="comment-user userinfo">Dominc</span>
</div>
</div>
</div>
<div id="comment-tools-16923" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16923-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

