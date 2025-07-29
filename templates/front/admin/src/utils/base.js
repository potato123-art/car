const base = {
    get() {
        return {
            url : "http://localhost:8080/django78p27/",
            name: "django78p27",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/django78p27/front/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "基于Python的车辆故障管理系统"
        } 
    }
}
export default base
