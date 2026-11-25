
import streamlit as st

# =====================================
# 페이지 설정
# =====================================

st.set_page_config(
    page_title="유민수 상병 구하기",
    page_icon="🎖️",
    layout="centered"
)

# =====================================
# CSS 디자인
# =====================================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(150deg, #101820, #263746);
    color: white;
}

h1, h2, h3, p, label {
    color: white !important;
}

.stButton button {
    width: 100%;
    min-height: 55px;
    border-radius: 12px;
    background-color: #d6a84b;
    color: #111111;
    font-size: 17px;
    font-weight: bold;
    border: none;
    margin-top: 5px;
}

.stButton button:hover {
    background-color: #f2c766;
    color: black;
}

div[data-testid="stAlert"] {
    border-radius: 12px;
}

hr {
    border-color: #607080;
}
</style>
""", unsafe_allow_html=True)


# =====================================
# 게임 상태 초기화
# =====================================

def restart():
    st.session_state.page = "intro"
    st.session_state.role = None
    st.session_state.gender = None
    st.session_state.message = ""
    st.session_state.ending = None


if "page" not in st.session_state:
    restart()


def go(page):
    st.session_state.page = page


def ending(title, message, success=False):
    st.session_state.ending = {
        "title": title,
        "message": message,
        "success": success
    }
    go("ending")


# =====================================
# 인트로 화면
# =====================================

if st.session_state.page == "intro":

    st.title("🎖️ 유민수 상병 구하기")
    st.subheader("긴급 인질 구출 작전")

    st.warning(
        "유민수 상병이 정체불명의 무장 세력에게 납치되었습니다."
    )

    st.write(
        "당신의 선택에 따라 유민수 상병의 운명이 결정됩니다."
    )

    st.divider()

    st.markdown("### 작전을 시작하시겠습니까?")

    if st.button("▶ 작전 시작"):
        go("role")


# =====================================
# 역할 선택
# =====================================

elif st.session_state.page == "role":

    st.title("작전 담당자 선택")
    st.write("당신이 맡을 역할을 선택하세요.")

    if st.button("🤝 협상가"):
        st.session_state.role = "협상가"
        go("gender")

    if st.button("⭐ 장성"):
        st.session_state.role = "장성"
        go("gender")

    if st.button("🚔 경찰"):
        st.session_state.role = "경찰"
        go("gender")


# =====================================
# 성별 선택
# =====================================

elif st.session_state.page == "gender":

    st.title("성별 선택")

    if st.button("남자"):
        st.session_state.gender = "남자"
        go("situation")

    if st.button("여자"):
        st.session_state.gender = "여자"
        go("situation")


# =====================================
# 납치 상황
# =====================================

elif st.session_state.page == "situation":

    st.title("🚨 긴급 상황 발생")

    st.error("유민수 상병이 납치되었습니다!")

    st.write(
        "납치범들이 유민수 상병을 인질로 잡고 있습니다."
    )

    st.info(f"담당 역할: {st.session_state.role}")
    st.info(f"성별: {st.session_state.gender}")

    if st.button("상황 확인"):
        if st.session_state.role == "협상가":
            go("negotiator")

        elif st.session_state.role == "장성":
            go("general")

        elif st.session_state.role == "경찰":
            go("police")


# =====================================
# 협상가 화면
# =====================================

elif st.session_state.page == "negotiator":

    st.title("🤝 협상가 작전실")

    st.warning("납치범이 몸값 100만 달러를 요구합니다.")

    if st.button("1번. 몸값 100만 달러 지불"):

        ending(
            "임무 성공",
            "몸값을 지불하고 유민수 상병을 구출했습니다. "
            "하지만 독단적인 몸값 지불로 보직해임되었습니다.",
            True
        )

    if st.button("2번. 몸값 지불 거부"):

        go("kidney")

    if st.button("3번. 몸값 인하 요청"):

        go("discount")

    st.divider()

    st.subheader("직접 협상하기")

    custom = st.text_input(
        "납치범에게 전달할 협상 내용을 입력하세요."
    )

    if st.button("협상 내용 전달"):

        if custom.strip():

            st.session_state.message = custom
            go("custom_result")

        else:
            st.warning("협상 내용을 입력하세요.")


# =====================================
# 몸값 인하 협상
# =====================================

elif st.session_state.page == "discount":

    st.title("📉 몸값 인하 협상")

    st.write("얼마나 인하를 요청하시겠습니까?")

    if st.button("10% 인하 요청"):

        ending(
            "임무 성공",
            "납치범이 협상을 받아들였습니다. "
            "몸값을 지불하고 유민수 상병을 구출했지만 "
            "보직해임되었습니다.",
            True
        )

    if st.button("20% 인하 요청"):

        ending(
            "임무 성공",
            "협상이 타결되어 유민수 상병을 구출했습니다. "
            "하지만 몸값 지불로 인해 보직해임되었습니다.",
            True
        )

    if st.button("70% 인하 요청"):

        go("kidney")


# =====================================
# 콩팥 손상 이후 4가지 선택
# =====================================

elif st.session_state.page == "kidney":

    st.title("⚠️ 협상 결렬")

    st.error(
        "납치범이 협상에 분노했습니다. "
        "유민수 상병은 콩팥 하나를 잃었습니다."
    )

    st.warning(
        "긴급 상황입니다. 다음 4가지 대응 중 하나를 선택하세요."
    )

    st.divider()

    # 1번
    if st.button("1번. 의료 지원 및 후송"):

        ending(
            "구출 성공",
            "의료 지원팀이 도착했습니다. "
            "유민수 상병을 병원으로 안전하게 후송했습니다.",
            True
        )

    # 2번
    if st.button("2번. 재협상 시도"):

        ending(
            "작전 실패",
            "재협상이 결렬되었습니다. "
            "결국 유민수 상병이 사망했습니다."
        )

    # 3번
    if st.button("3번. 군경 합동 대응"):

        ending(
            "구출 성공",
            "군경 합동 작전으로 유민수 상병을 구출했습니다. "
            "하지만 심각한 부상과 후유증이 남았습니다.",
            True
        )

    # 4번
    if st.button("4번. 아무것도 하지 않는다"):

        ending(
            "작전 실패",
            "아무런 조치도 취하지 않은 결과, "
            "유민수 상병이 사망했습니다."
        )


# =====================================
# 직접 협상 결과
# =====================================

elif st.session_state.page == "custom_result":

    st.title("📡 협상 결과")

    st.write("당신이 전달한 협상 내용:")

    st.info(st.session_state.message)

    message = st.session_state.message

    if any(word in message for word in [
        "구출", "석방", "협력", "협상"
    ]):

        st.success("납치범이 대화에 응했습니다.")

        if st.button("협상 계속하기"):

            ending(
                "구출 성공",
                "협상이 타결되어 유민수 상병을 구출했습니다.",
                True
            )

    elif any(word in message for word in [
        "공격", "죽여", "체포", "진압"
    ]):

        st.error("납치범이 위협을 느끼고 협상을 중단했습니다.")

        if st.button("상황 확인"):
            go("kidney")

    else:

        st.warning("납치범이 답변을 이해하지 못했습니다.")

        if st.button("다시 협상하기"):
            go("negotiator")


# =====================================
# 장성 화면
# =====================================

elif st.session_state.page == "general":

    st.title("⭐ 장성 작전실")

    st.warning(
        "군대를 투입하여 유민수 상병을 구출하시겠습니까?"
    )

    if st.button("군대 투입"):

        ending(
            "구출 성공",
            "군 작전이 성공하여 유민수 상병을 구출했습니다. "
            "하지만 심각한 신체 부상과 장기적인 후유증이 남았습니다.",
            True
        )


# =====================================
# 경찰 화면
# =====================================

elif st.session_state.page == "police":

    st.title("🚔 경찰 작전실")

    st.write("경찰은 어떤 조치를 취하시겠습니까?")

    if st.button("1번. 구출 작전 실행"):

        ending(
            "구출 성공",
            "경찰 특공대의 작전이 성공했습니다. "
            "유민수 상병을 무사히 구출했습니다.",
            True
        )

    if st.button("2번. 사건 무시"):

        ending(
            "작전 실패",
            "사건이 방치되는 동안 유민수 상병이 사망했습니다."
        )

    if st.button("3번. 수배 명단 등록"):

        ending(
            "구출 성공",
            "수배 명단 등록 후 군대가 투입되었습니다. "
            "유민수 상병을 구출했지만 심각한 부상과 후유증이 남았습니다.",
            True
        )


# =====================================
# 엔딩 화면
# =====================================

elif st.session_state.page == "ending":

    result = st.session_state.ending

    st.title(result["title"])

    if result["success"]:

        st.success(result["message"])
        st.balloons()

    else:

        st.error("실패입니다. 다시 시도하세요.")
        st.write(result["message"])

    st.divider()

    if st.button("🔄 처음부터 다시 시작"):

        restart()
        st.rerun()


# =====================================
# 하단 문구
# =====================================

st.divider()

st.caption(
    "유민수 상병 구하기 | 선택형 스토리 게임"
)
