+++
type = "question"
title = "Dueling Dissectors"
description = '''I&#x27;m guessing there are many ways to solve this, but so far I&#x27;m coming up dry... I have two different dissector instances which differ in terms of a layer of protocol/wrapper which either exists or does not. Unfortunately there&#x27;s no way to easily determine whether this wrapper exists which is why I h...'''
date = "2017-06-16T10:53:00Z"
lastmod = "2017-06-18T12:23:00Z"
weight = 62058
keywords = [ "dissector_add_uint", "dissector" ]
aliases = [ "/questions/62058" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dueling Dissectors](/questions/62058/dueling-dissectors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62058-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62058-score" class="post-score" title="current number of votes">0</div><span id="post-62058-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm guessing there are many ways to solve this, but so far I'm coming up dry...</p><p>I have two different dissector instances which differ in terms of a layer of protocol/wrapper which either exists or does not. Unfortunately there's no way to easily determine whether this wrapper exists which is why I had intend to create two dissector instances which differ chiefly in this regard.</p><p>The problem is that it seems that I cannot use the "enabled protocols" feature to effectively switch between which type of data should be expected. When I disable one of the two protocols it seems to not "fail over" to uses the alternative despite them both using the same registration methods (dissector_add_uint).</p><p>I've found that in order to "fail over" to the alternative dissector I need to actually remove the alternate plug-in from the search path; this is not a tenable solution.</p><p>So any suggestions on how to proceed? - Is there some way to do an effective parallel registration? - Are there callback methods I can register to be notified of enable/disable operations (so that I could register/de-register as a workaround) - Perhaps merging the two dissectors and governing behavior based on a preference is simpler?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector_add_uint" rel="tag" title="see questions tagged &#39;dissector_add_uint&#39;">dissector_add_uint</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jun '17, 10:53</strong></p><img src="https://secure.gravatar.com/avatar/f5a6a32440657fdf63b9db18f3922c70?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wittynickname&#39;s gravatar image" /><p><span>wittynickname</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wittynickname has one accepted answer">50%</span></p></div></div><div id="comments-container-62058" class="comments-container"></div><div id="comment-tools-62058" class="comment-tools"></div><div class="clear"></div><div id="comment-62058-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62059"></span>

<div id="answer-container-62059" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62059-score" class="post-score" title="current number of votes">0</div><span id="post-62059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Look into heuristic dissectors. They have to determine, after reading an initial part of the packet, it it's theirs to keep of that some other dissector may have a stab at it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jun '17, 12:03</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-62059" class="comments-container"><span id="62062"></span><div id="comment-62062" class="comment"><div id="post-62062-score" class="comment-score"></div><div class="comment-text"><p>I gave some thought to attempting that, but was worried I might be painted into a corner in terms of performance. Particularly if I need to run CRC checks to be certain of a match, etc.</p><p>After consulting with some users I'm going to just go the preference route</p></div><div id="comment-62062-info" class="comment-info"><span class="comment-age">(16 Jun '17, 13:09)</span> <span class="comment-user userinfo">wittynickname</span></div></div><span id="62097"></span><div id="comment-62097" class="comment"><div id="post-62097-score" class="comment-score"></div><div class="comment-text"><p>A heuristic dissector doesn't necessarily have to run all the checks on each frame, it is enough to do that on a first one of each "session".</p><p>As for callback methods to be registered - the "core" normally invokes a dedicated function of your dissector code each time a setting is changed in the GUI (and once during initialization). I only write Lua dissectors where the function is called <code>&lt;protocol_object_name&gt;.prefs_changed()</code>, so you'll have to find out the equivalent if you use C.</p></div><div id="comment-62097-info" class="comment-info"><span class="comment-age">(18 Jun '17, 03:08)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="62104"></span><div id="comment-62104" class="comment"><div id="post-62104-score" class="comment-score"></div><div class="comment-text"><p>Hm, it is not that easy. I did what I'd suggested and it didn't work: when I switched the preference "use" of one of the dissectors to <code>false</code>, which invoked a <code>dissector_table:remove</code> for it and I could see that the item has indeed disappeared from the dissector table listing, and then switched the preference "use" of the other dissector to <code>true</code>, the other one did not appear in the dissector table - while it does if the first dissector is removed from the plugins.</p><p>So it <strong>seems</strong> to me as if the <code>&lt;protocol_object_name&gt;.prefs_changed()</code> function is called for <strong>all</strong> protocols in alphabetical order each time a preference of <strong>any</strong> of them is changed.</p><p>In C it should be easy for you to check, before removing a dissector from the table, whether it is the one you've put there yourself (so you can remove it) or some other one (so you should not touch it). In Lua it seems impossible to me so far as the <code>==</code> test fails on both <code>protocol_name</code> and <code>protocol_name.dissector</code>.</p></div><div id="comment-62104-info" class="comment-info"><span class="comment-age">(18 Jun '17, 11:36)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="62108"></span><div id="comment-62108" class="comment"><div id="post-62108-score" class="comment-score"></div><div class="comment-text"><p>Solved that by a workaround, so the whole solution in Lua now looks like this:</p><pre><code>-- in the Main Code of the Module
local it_is_me = false

-- Handling of Preference Changes
function my_proto.prefs_changed()
    local my_dis_table = DissectorTable.get(&quot;parent_proto.selector_value&quot;)
    if my_proto.prefs[&quot;use&quot;] then
        my_dis_table:add(value,my_proto)
        it_is_me = true
    else
        if it_is_me then
            my_dis_table:remove(value,my_proto)
            it_is_me = true
        end
    end
end</code></pre></div><div id="comment-62108-info" class="comment-info"><span class="comment-age">(18 Jun '17, 12:23)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-62059" class="comment-tools"></div><div class="clear"></div><div id="comment-62059-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

