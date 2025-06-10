+++
type = "question"
title = "[closed] OpenLayers.Filter.Function is not working as expected. In fact, not at all working"
description = '''I&#x27;m trying to set up a Rule using the Function Filter. But it does not work: the lines on that layer are just black. More importantly, the function that I provide to filter the features, is never called. Can someone please point out what is the mistake that i&#x27;m making? Here is the code. Thank you fo...'''
date = "2012-07-23T22:18:00Z"
lastmod = "2012-07-23T22:18:00Z"
weight = 14523
keywords = [ "geocoding", "javascript", "openlayers" ]
aliases = [ "/questions/14523" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] OpenLayers.Filter.Function is not working as expected. In fact, not at all working](/questions/14523/openlayersfilterfunction-is-not-working-as-expected-in-fact-not-at-all-working)

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
<span id="post-14523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14523-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to set up a Rule using the Function Filter. But it does not work: the lines on that layer are just black. More importantly, the function that I provide to filter the features, is never called.</p>
<p>Can someone please point out what is the mistake that i'm making?</p>
<p>Here is the code.</p>
<p>Thank you for your time and kind concern.<br />
</p>
<pre><code>var my_filter = new OpenLayers.Filter.Function(
    function(attributes) {
       console.log(attributes);
       var x=0; 
       return true; 
});
&#10;var ruleLow = new OpenLayers.Rule({
    filter:my_filter ,
  symbolizer: {pointRadius: 10, fillColor: &quot;green&quot;,
               fillOpacity: 0.5, strokeColor: &quot;green&quot;}
});
&#10;var my_style=new OpenLayers.Style( null,ruleLow);
&#10;var my_style_map=new OpenLayers.StyleMap({
    &quot;temporary&quot;:my_style,
    &quot;default&quot;:my_style,
    &quot;select&quot;:my_style
});
&#10;this.vectors= new OpenLayers.Layer.Vector(
    &quot;Vector Layer&quot;,
    {
        styleMap:my_style_map,
        renderers:this.renderer,
    }
);</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jul '12, 22:18</strong></p>
<img src="https://secure.gravatar.com/avatar/9dd74c6b4fbba97f31218e1dd311177c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jenia&#39;s gravatar image" />
<p><span>jenia</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jenia has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>24 Jul '12, 08:46</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-14523" class="comments-container">
&#10;</div>
<div id="comment-tools-14523" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14523-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "This is not an OpenLayers support forum. See www.openlayers.org for mailing lists and other ways to get in touch." by Frederik Ramm 24 Jul '12, 08:46

</div>

</div>

</div>

