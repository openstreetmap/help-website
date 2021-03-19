+++
type = "question"
title = "Better JSON access?"
description = '''Surely there&#x27;s got to be a better way to dump out the JSON text that this? ...Stu do  local json_fe = Field.new(&quot;json&quot;) local tap = Listener.new(&quot;http&quot;, &quot;http.content_type contains &#92;&quot;json&#92;&quot;&quot;)  function decode(c)  return string.char(tonumber(c, 16)) end  function tap.reset() end  function tap.packet(...'''
date = "2011-12-08T00:51:00Z"
lastmod = "2014-09-08T00:47:00Z"
weight = 7843
keywords = [ "lua", "json" ]
aliases = [ "/questions/7843" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Better JSON access?](/questions/7843/better-json-access)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7843-score" class="post-score" title="current number of votes">0</div><span id="post-7843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Surely there's got to be a better way to dump out the JSON text that this?</p><p>...Stu</p><pre><code>do
    local json_fe = Field.new(&quot;json&quot;)
local tap = Listener.new(&quot;http&quot;, &quot;http.content_type contains \&quot;json\&quot;&quot;)

function decode(c)
    return string.char(tonumber(c, 16))
end

function tap.reset()
end

function tap.packet(pinfo, tvb, ip)
    local json = json_fe()

    -- The extra ()s in the next line is to discard the second returned value from gsub
    -- We only want to output the json object
    print((tostring(json.value):gsub(&quot;(%x%x)&quot;, decode)))
end

function tap.draw()
end</code></pre><p>end</p></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-json" rel="tag" title="see questions tagged &#39;json&#39;">json</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Dec '11, 00:51</strong></p><img src="https://secure.gravatar.com/avatar/88d413834375dbc71f5d3146aca1cd3c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="studog&#39;s gravatar image" /><p><span>studog</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="studog has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Dec '11, 00:52</strong> </span></p></div></div><div id="comments-container-7843" class="comments-container"></div><div id="comment-tools-7843" class="comment-tools"></div><div class="clear"></div><div id="comment-7843-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36061"></span>

<div id="answer-container-36061" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36061-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36061-score" class="post-score" title="current number of votes">1</div><span id="post-36061-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There you go:</p><pre><code>function tap.packet(pinfo, tvb, ip)
  local json = json_fe();
  if (json ~= nil) then
    local tvbrange = json.range;
    local json_string = tvbrange:string();
  end
end</code></pre><p>I think I've wasted some 2 days over this... issue. Jacek</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Sep '14, 00:47</strong></p><img src="https://secure.gravatar.com/avatar/23ba391bf726a3714542d3fd46f0b56f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jacek&#39;s gravatar image" /><p><span>Jacek</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jacek has no accepted answers">0%</span></p></div></div><div id="comments-container-36061" class="comments-container"></div><div id="comment-tools-36061" class="comment-tools"></div><div class="clear"></div><div id="comment-36061-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

