+++
type = "question"
title = "Add ERROR COLOR to a dissector"
description = '''Hi, i´am nearly ready with my own dissector. At least i want to colorize my the table-row from a mailformed frame. How can i do this? actual Error Routine:  local Frame_OK = 1 if buffer:len() &amp;lt; 10 then   Frame_OK = 0   TreeNode = TreeNode_E1:add(buffer(), &quot;Payload-Data integrity : &quot; .. &quot;ERROR - p...'''
date = "2011-06-09T12:31:00Z"
lastmod = "2011-06-10T10:01:00Z"
weight = 4474
keywords = [ "color-rules", "lua", "dissector", "coloring" ]
aliases = [ "/questions/4474" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Add ERROR COLOR to a dissector](/questions/4474/add-error-color-to-a-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4474-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4474-score" class="post-score" title="current number of votes">0</div><span id="post-4474-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i´am nearly ready with my own dissector. At least i want to colorize my the table-row from a mailformed frame.</p><p>How can i do this?</p><p>actual Error Routine:</p><pre><code>    local Frame_OK = 1
if buffer:len() &lt; 10 then 
      Frame_OK = 0 
      TreeNode = TreeNode_E1:add(buffer(), &quot;Payload-Data integrity : &quot; .. &quot;ERROR - payload Length &lt; 10 bytes!&quot; )
    end
if Frame_OK == 1 then
      if not (buffer(0,1):uint() == 91)  
         or not (buffer(8,1):uint() == 124) 
         or not (buffer(buffer:len()-1,1):uint() == 93) then   
        Frame_OK = 0 
        TreeNode = TreeNode_E1:add(buffer(), &quot;Payload-Data integrity : &quot; .. &quot;ERROR - identifyer mismatch! &quot; )   
      end
    end  
    if Frame_OK == 1 then
      TreeNode = TreeNode_E1:add(buffer(), &quot;Payload-Data integrity : &quot; .. &quot;OK&quot; ) 
    end</code></pre><p>thanks for your help... Pfanne</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-color-rules" rel="tag" title="see questions tagged &#39;color-rules&#39;">color-rules</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-coloring" rel="tag" title="see questions tagged &#39;coloring&#39;">coloring</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '11, 12:31</strong></p><img src="https://secure.gravatar.com/avatar/99abe74976c1c0ca886da31fed9feaa1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pfanne&#39;s gravatar image" /><p><span>Pfanne</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pfanne has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> retagged <strong>10 Jun '11, 18:18</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-4474" class="comments-container"></div><div id="comment-tools-4474" class="comment-tools"></div><div class="clear"></div><div id="comment-4474-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4478"></span>

<div id="answer-container-4478" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4478-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4478-score" class="post-score" title="current number of votes">2</div><span id="post-4478-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use the expert system to mark the malformed part of the frame. See <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/expert.h">epan/expert.h</a>. The severity of the expert message will determine it's color. In case of a malformed PDU, the proper group would be "PI_MALFORMED" with severity "Error".</p><p>See also: <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChAdvExpert.html">http://www.wireshark.org/docs/wsug_html_chunked/ChAdvExpert.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '11, 13:18</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Jun '11, 13:18</strong> </span></p></div></div><div id="comments-container-4478" class="comments-container"><span id="4479"></span><div id="comment-4479" class="comment"><div id="post-4479-score" class="comment-score"></div><div class="comment-text"><p>Oops, I just noticed that you use LUA, I'm not sure the LUA-API does include the expert info stuff too... Maybe someone else can answer that...</p></div><div id="comment-4479-info" class="comment-info"><span class="comment-age">(09 Jun '11, 13:19)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="4480"></span><div id="comment-4480" class="comment"><div id="post-4480-score" class="comment-score"></div><div class="comment-text"><p>Hi, thank´s for your fast answers.</p><p>I have seen your links also bevor, my problem ist the lua-syntax. Can you give me a specific hint in my code?</p></div><div id="comment-4480-info" class="comment-info"><span class="comment-age">(09 Jun '11, 13:25)</span> <span class="comment-user userinfo">Pfanne</span></div></div><span id="4483"></span><div id="comment-4483" class="comment"><div id="post-4483-score" class="comment-score">1</div><div class="comment-text"><p>You should be able to use the Lua "set_expert_flags" or "add_expert_info" methods on a Treeitem; see <a href="http://wiki.wireshark.org/LuaAPI/TreeItem">the Lua API entry for Treeitem</a>.</p></div><div id="comment-4483-info" class="comment-info"><span class="comment-age">(09 Jun '11, 13:35)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="4510"></span><div id="comment-4510" class="comment"><div id="post-4510-score" class="comment-score"></div><div class="comment-text"><pre><code>TreeNode = TreeNode_E1:add_expert_info(PI_MALFORMED, PI_ERROR, &quot;identifyer mismatch!&quot;)</code></pre><p>that´s it, very usefull hint!, thank´s Guy Harris.</p><p>My UDP-Command-dissactor is ready!!!</p><p>Thank´s to all people who help me.</p><p>Greets from Hamburg Pfanne</p></div><div id="comment-4510-info" class="comment-info"><span class="comment-age">(10 Jun '11, 10:01)</span> <span class="comment-user userinfo">Pfanne</span></div></div></div><div id="comment-tools-4478" class="comment-tools"></div><div class="clear"></div><div id="comment-4478-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4476"></span>

<div id="answer-container-4476" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4476-score" class="post-score" title="current number of votes">1</div><span id="post-4476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You colorize packets by adding a color rule that matches something you put into the protocol tree for the error.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '11, 12:57</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-4476" class="comments-container"><span id="4481"></span><div id="comment-4481" class="comment"><div id="post-4481-score" class="comment-score"></div><div class="comment-text"><p>to Guy Harris</p><p>is there no way to integrate the color error into my lua-code?</p></div><div id="comment-4481-info" class="comment-info"><span class="comment-age">(09 Jun '11, 13:27)</span> <span class="comment-user userinfo">Pfanne</span></div></div><span id="4482"></span><div id="comment-4482" class="comment"><div id="post-4482-score" class="comment-score"></div><div class="comment-text"><p>There's no way for a dissector to directly do anything about color, as the environment in which dissectors run knows nothing about color (by design - there's no guarantee that the output of the dissector will be in an environment where things can be colored, and the user should be allowed to control colorization in any case).</p></div><div id="comment-4482-info" class="comment-info"><span class="comment-age">(09 Jun '11, 13:32)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-4476" class="comment-tools"></div><div class="clear"></div><div id="comment-4476-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

